GPTQ output

↓

INT4 weights
+ scales

--------------------------------

Inference

Y = WX

W = sQ

--------------------------------

Compute

Y = s(QX)

--------------------------------

Do NOT reconstruct
full FP16 weights.

--------------------------------

Use specialized
quantized GEMM kernels.

--------------------------------

Weights remain INT4
until computation.

--------------------------------

Activations remain FP16/BF16.

--------------------------------

Output usually FP16.

--------------------------------

Main benefit:

Less HBM traffic.

--------------------------------

LLM inference is often
memory-bound.

Therefore quantization
improves throughput
and reduces memory usage.
