## Why doesn't a 7B parameter model require only 14GB to train?

Naive Calculation:

7B parameters × 2 bytes (FP16)

≈ 14GB

This only accounts for model weights.

Actual Training Memory Includes:

Parameters
Model weights
≈ 14GB
Gradients
One gradient per parameter
≈ 14GB
Optimizer States (AdamW)
Momentum (m)
Variance estimate (v)
Often stored in FP32
Can consume more memory than the weights themselves
Activations
Q, K, V
Attention outputs
FFN outputs
Layer outputs
Stored for backpropagation

## Important Insight

Parameter memory depends on:

Model Size

Activation memory depends on:

Batch Size
×
Sequence Length
×
Layers
×
Hidden Dimension

## Deep Intuition

Parameters store learned knowledge.

Activations store temporary computations.

Gradients store error information.

Optimizer states store training history.

Training requires all of them simultaneously, which is why actual training memory is often many times larger than parameter memory alone.
