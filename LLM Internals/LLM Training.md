## What does one GPT training example look like?

Language modeling objective:

Predict the next token given previous tokens.

Example sentence:

"I love deep learning"

Input sequence:

I
love
deep
learning

Target sequence:

love
deep
learning <eos>

Targets are shifted by one position.

This allows GPT to learn next-token prediction at every position simultaneously.

Pipeline:

1. Tokenization

Tokens → Token IDs

Shape:
(sequence_length)

Example:
(4)

2. Embedding Layer

Embedding Matrix:
(vocab_size, hidden_dim)

Example:
(50000, 768)

Output:
(sequence_length, hidden_dim)

Example:
(4, 768)

3. Positional Encoding

Added to embeddings.

Shape remains:
(4, 768)

4. Transformer Layers

Attention
→ FFN
→ Residual Connections
→ LayerNorm

Shape remains:
(4, 768)

Representations become richer at each layer.

5. Final Hidden States

Output shape:
(4, 768)

These are contextual representations for each token.

## After transformer layers produce rich contextual representations, how do those vectors become actual word predictions?

Reasoning:

The model's goal is next-token prediction.

After the final transformer layer, each token position has a contextual representation.

Example:

"I love deep"

may become a 768-dimensional vector containing information about:

* Meaning
* Grammar
* Context
* Relationships
* Prediction clues

But the model must finally answer:

"What is the next word?"

Vocabulary may contain 50,000 words.

So we need:

768 dimensions
→
50,000 scores

Researchers add a final linear layer called the LM Head.

LM Head:

Hidden State
→
Vocabulary Scores

Shape:

(768)
→
(50000)

Output is called Logits.

Logits are raw scores, not probabilities.

Example:

learning → 12.3

dog → 4.1

cat → 2.0

These scores are converted into probabilities using Softmax.

Now the model predicts:

P(next token | context)

Example:

learning → 92%

dog → 1%

cat → 0.5%

Now researchers need to measure:

"How good was this prediction?"

If the true next word is "learning", then:

High probability for "learning"
→ small loss

Low probability for "learning"
→ large loss

This leads to Cross Entropy Loss, which becomes the training signal used for learning.

Key Insight:

Transformer layers learn representations.

LM Head converts representations into vocabulary scores.

Softmax converts scores into probabilities.

Cross Entropy tells the model how wrong its prediction was.


## Why is GPT trained using Cross Entropy Loss −log(p) instead of 1−p or squared error?

The model predicts a probability distribution over the vocabulary. We need a loss that:

Is small when the correct word gets high probability.
Is large when the correct word gets low probability.
Punishes confident mistakes very strongly.
Produces stable gradients for training.

## Why not 1−p?

It treats:

0.90 → 0.99

and

0.01 → 0.10

as similar improvements, even though the second is much more important.

## Why not MSE?

It works, but does not interact as naturally with probability distributions and softmax. Gradients are less suitable for classification problems.

## Why −log(p)?

Because:

p=1 gives loss 0
Small probabilities produce very large losses
Confidently wrong predictions are punished heavily

It comes directly from information theory

Deep Intuition:

Cross Entropy measures how surprised the model is by the correct answer.

The more surprised the model is when the true token appears, the larger the loss and the stronger the learning signal.


## We computed Cross Entropy Loss. How does that single number update billions of Transformer parameters?

Core Idea:

The loss tells us how wrong the prediction was.

But to learn, the model must know:

"If I change a particular weight slightly, will the loss increase or decrease?"

This quantity is called the Gradient.

Gradient: dLoss / dWeight

Meaning: How sensitive is the loss to that weight?

Positive gradient:
Increasing the weight increases loss.

Negative gradient:
Increasing the weight decreases loss.

Backpropagation:

Forward Pass:
Input → Transformer → Prediction → Loss

Backward Pass:
Loss → Gradients → Every Parameter

The backward pass assigns blame for the error.

Important Insight:

Forward pass computes representations.

Backward pass computes responsibility for mistakes.

## Why Activations Are Stored:

To compute gradients, the model needs the intermediate outputs from every layer.

Therefore during training:

Layer Outputs (Activations)
are stored in memory.

This is one major reason LLM training requires huge GPU memory.

Parameter Update:

After gradients are computed:

New Weight = Old Weight − Learning Rate × Gradient

This process repeats over billions of training examples.

## Deep Intuition:

The model is not explicitly taught language rules.

Instead, every example produces tiny corrections to billions of weights.

Over time these corrections accumulate into language understanding, reasoning ability, coding skills, and other capabilities.

## What are activations, why do they dominate training memory, and how can we estimate Transformer parameters?

Parameters:
Learnable weights stored permanently in the model.

Examples:
WQ, WK, WV, WO, FFN weights, Embeddings.

Activations:
Intermediate outputs produced while processing a specific input batch.

Activations depend on the current input.
Parameters do not.

## Why Save Activations?

During backpropagation, gradients require intermediate values from the forward pass.

Examples:

To compute gradients through attention, we need:
Q, K, V, attention scores, softmax outputs, FFN outputs, etc.

Therefore these tensors must be stored during training.

## Why Training Uses More Memory Than Inference

Inference:
Forward pass only.
Most activations can be discarded.

Training:
Forward pass + Backward pass.
Activations must be stored until gradients are computed.

Hence training memory is much larger.

Attention Memory

Attention scores have shape:

(Batch, Heads, Sequence, Sequence)

This introduces:

O(Sequence²)

memory growth.

This is one reason long-context training becomes expensive.

Parameter Estimation

Embedding Layer:

Parameters = Vocabulary Size × Hidden Dimension

Attention Block: WQ + WK + WV + WO ≈ 4D²

FFN Block: D → 4D → D ≈ 8D²

Total Transformer Layer: ≈ 12D²

Entire Model: ≈ 12 × Layers × D² * Embedding Parameters

## Important Insight:

Most Transformer parameters are usually in the FFN layers, not the attention layers.

## Deep Intuition:

Parameters store learned knowledge.

Activations store temporary computations needed to calculate gradients.

Large context lengths and batch sizes make activation memory explode, which is why activations often dominate training memory.
