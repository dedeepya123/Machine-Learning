## Why Weight Quantization Alone Is Not Enough
- Weights become much smaller after INT4, but activations remain FP16.
- Activation tensors are large and repeatedly created at every transformer layer.
- Computation is still mixed precision (INT4 weights × FP16 activations), so hardware cannot fully benefit from low-precision arithmetic.
- Activation memory and bandwidth become a significant bottleneck once weights are compressed.

## Why Activations Are Much Harder to Quantize
        Weights	                                       Activations     
- Static after training  	                Change every token and every prompt
- Quantized once offline	                Must be quantized during inference-
- Stable distribution	                    Input-dependent distribution
- Plenty of offline optimization time	          Must run in real time
- Few severe outliers	                        Frequent activation outliers

## The Big Insight
Weight quantization asks:

How do we compress
a fixed tensor?

Activation quantization asks:

How do we compress
a tensor that changes
every forward pass?

That is a fundamentally different problem.
