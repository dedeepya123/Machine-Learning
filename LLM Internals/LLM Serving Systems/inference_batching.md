## Training also batches sequences of different lengths. Why is inference batching harder?

Training:

* Entire dataset is already available.
* Batches are created beforehand.
* Padding handles different sequence lengths.
* Batch size remains fixed.
* All samples move through forward and backward pass together.

Inference:

* Requests arrive continuously.
* Batch size changes dynamically.
* Output lengths are unknown beforehand.
* Some requests finish early.
* New requests arrive while others are still running.
* Each request has its own KV cache and sequence length.

Deep Insight:

Training batching is static.

Inference batching is dynamic.

This dynamic nature is the main reason serving systems are much more complicated than training systems.
