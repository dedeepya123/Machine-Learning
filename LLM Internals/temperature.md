## What is Temperature and why does it affect generation?

Model Output:

The Transformer produces logits, not probabilities.

Probabilities are obtained using Softmax.

Researcher Goal: Control how random or deterministic generation should be.

Idea:

Modify logits before Softmax.

Formula:

p_i = exp(z_i / T) / Σ exp(z_j / T)

where T is Temperature.

Case 1:

T = 1

Normal Softmax.

Nothing changes.

Case 2:

T < 1

Dividing by a small number increases differences between logits.

Softmax becomes more confident.

Distribution becomes sharper.

Effect:

* More deterministic
* Less random
* Closer to Greedy Decoding

Deep Intuition:

Low temperature says:

"Trust the model's highest-scoring token more."

Case 3:

T > 1

Dividing by a large number reduces differences between logits.

Softmax becomes less confident.

Distribution becomes flatter.

Effect:

* More diverse
* More creative
* More random

Deep Intuition:

High temperature says:

"Allow alternative tokens more opportunity."

Extreme Cases:

T → 0

Approaches Greedy Decoding.

T → ∞

Approaches a uniform distribution.

Problem Researchers Found:

Temperature increases diversity but also increases the probability of low-quality tokens.

Researchers wanted:

More diversity without allowing obviously bad tokens.

This led to Top-k Sampling.
