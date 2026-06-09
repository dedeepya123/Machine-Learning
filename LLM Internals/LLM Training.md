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
