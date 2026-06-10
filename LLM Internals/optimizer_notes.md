## Why was SGD insufficient for Transformers, and what exactly does AdamW add?

Researcher Observation: SGD updates weights using only the current gradient.

Update: w = w - lr × g
### Problems:
1. No memory of previous directions.
2. Same learning rate for all parameters.
3. Large gradients cause huge updates.
4. Tiny gradients cause almost no updates.

First Improvement: Momentum

Idea: Remember previous gradients.

Momentum (m) stores a running average of gradient directions.

"Where have gradients been consistently pointing?"

Effect:

* Less oscillation
* Smoother optimization
* Faster convergence

But momentum still uses the same learning rate for every parameter.

## Second Improvement: Adaptive Learning Rates

Researchers observed: Different Transformer parameters receive gradients with very different magnitudes.

Some may receive:

g = 50

Others:

g = 0.00001

Using the same learning rate causes unstable optimization.

Adam introduces:

v = running average of g²

"How large are gradients usually for this parameter?"

Effect:
Large historical gradients:
→ Smaller effective updates

Small historical gradients:
→ Larger effective updates

Deep Intuition:

m decides direction.

v decides caution.

Adam Update Intuition:

Move in the direction suggested by momentum.

Scale the step size according to historical gradient magnitudes.

## Why Transformers Benefit:

Transformers contain many different components:

* Embeddings
* Attention
* FFN
* LayerNorm

Gradient scales vary significantly across them.

Adam automatically adapts to these differences.

## Why AdamW?

Researchers discovered that L2 regularization interacts poorly with Adam's adaptive scaling.

Solution:

Separate weight decay from gradient computation.

Perform:

1. Adam update
2. Explicit weight shrinking

This became AdamW.

Final Mental Model:

SGD:
Current gradient.

Momentum:
Current gradient + direction history.

Adam:
Current gradient + direction history + magnitude history.

AdamW:
Adam + proper weight decay.

This is why AdamW became the standard optimizer for modern LLM training.


## Why do we need weight decay, and why was AdamW introduced?

Problem: Training only minimizes loss.

Nothing prevents weights from becoming unnecessarily large.

Large weights can lead to:

* Overfitting
* Memorization
* Poor generalization

Researcher Idea:

Prefer smaller weights when possible.

L2 Regularization:

Modified objective:

L_new = L + λ||W||²

Interpretation:

Term 1:
Fit the training data.

Term 2:
Penalize large weights.

Gradient:

dL_new/dW

=
dL/dW + 2λW

Important Insight:

The larger a weight becomes, the stronger the force pulling it back toward zero.

This creates weight decay.

With SGD:

Update becomes:

W = W - lr × gradient - lr × 2λW

Equivalent intuition:

Every step slightly shrinks the weights.

Why Adam Causes Issues:

Adam scales updates using:

m / √v

If L2 regularization is added into the gradient, the regularization term also gets scaled by Adam's adaptive statistics.

Weight shrinkage becomes entangled with adaptive learning rates.

Researchers wanted:

"Learning from data"

and

"Weight shrinking"

to be separate processes.

AdamW Solution:

Step 1:
Normal Adam update.

Step 2:
Explicitly shrink weights:

W = W - lr × λ × W

or

W = (1 - lrλ)W

Key Benefit:

Weight decay is independent of Adam's adaptive scaling.

Deep Intuition:

Adam learns useful patterns.

Weight decay prevents weights from becoming unnecessarily large.

AdamW combines both cleanly and became the standard optimizer for modern LLMs.
