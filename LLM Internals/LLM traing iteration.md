## One Complete LLM Training Iteration

1. Batch arrives

Raw text batch enters training pipeline.

2. Tokenization

Text → Token IDs

3. Embedding Lookup

Token IDs → Dense vectors

Shape:

(Batch, Sequence, Hidden Dimension)

4. Forward Pass Through Transformer

For every layer:

* Compute Q, K, V
* Attention
* Context vectors
* FFN
* Residual connections
* LayerNorm

Intermediate activations are stored for backpropagation.

5. Vocabulary Projection

Final hidden states are projected to vocabulary space.

Output:

Logits

Shape:

(Batch, Sequence, Vocabulary)

6. Softmax

Convert logits into probability distributions.

7. Cross Entropy Loss

Compare predicted probabilities with true next tokens.

Produces one scalar loss.

8. Backpropagation

Starting from the loss:

Compute gradients for every parameter.

Uses stored activations from the forward pass.

9. AdamW Update

For every parameter:

* Update momentum (m)
* Update variance estimate (v)
* Apply Adam update
* Apply weight decay

Parameters are updated.

10. Cleanup

* Activations freed
* Gradients cleared

GPU memory becomes available for next batch.

Deep Intuition:

Training is not teaching explicit rules.

Every batch produces tiny corrections to billions of parameters.

After billions of such updates, language understanding and reasoning capabilities emerge.
