# "Can you classify quantization methods?"
Based on 
## When do we quantize?
PTQ vs QAT.
## What do we quantize?
Weights, activations, or both.
## How do we represent values?
Symmetric vs asymmetric.
## What granularity do we use?
Per-tensor, per-channel, per-group.
## What optimization algorithm minimizes the error?
Naive PTQ → GPTQ → AWQ → SmoothQuant.

That hierarchy is how the field is organized, and once you have it, almost every quantization paper can be placed naturally into the correct branch.
