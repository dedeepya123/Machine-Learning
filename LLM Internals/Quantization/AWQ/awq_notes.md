Problem

GPTQ successfully quantizes LLMs but requires Hessian approximation and sequential second-order compensation, making it computationally expensive.

Key Observation

For a linear layer

Y=WX,

quantization error propagates as

ΔY=(ΔW)X.

Large activation channels amplify weight quantization errors much more than small activation channels.

Therefore, activation statistics naturally identify important input channels.

Core Idea

<img width="1106" height="491" alt="image" src="https://github.com/user-attachments/assets/1cbc5761-4033-4051-b2f7-95bb3f7d9366" />

Optimization Objective

<img width="847" height="275" alt="image" src="https://github.com/user-attachments/assets/1b8bb491-e62a-4dbf-8aa9-5c0f076ac536" />


## Advantages
No Hessian computation
No matrix inverse
No sequential compensation
Faster than GPTQ
Excellent INT4 accuracy
Preserves the most important channels before quantization rather than repairing errors afterward

## The Big Picture

Now look at the progression from the beginning of quantization:

Naive PTQ
│
├── Quantize everything equally
│
▼
OBD
│
├── Use Hessian diagonal
│
▼
OBS
│
├── Use full Hessian inverse
│
▼
GPTQ
│
├── Approximate Hessian with XXᵀ
├── Sequential compensation
│
▼
AWQ
│
├── Observe activation magnitudes
├── Protect important channels
├── Rescale before quantization
└── No Hessian required

Notice how the field evolved:

OBD/OBS asked: Which weights are sensitive?
GPTQ asked: How can I compensate for quantization error?
AWQ asked: How can I avoid creating large quantization error in the first place?
