# Smooth Quant
Activation quantization is significantly harder than weight quantization because activations are dynamic and contain large outlier channels. These outliers force coarse quantization scales, reducing precision for normal activation values. SmoothQuant observes that for a linear layer,

WX=(WS)(S−1X),

so the output is unchanged if weights and activations are inversely scaled. It uses calibration data to compute per-channel scaling factors that reduce activation outliers while proportionally increasing the corresponding weights. Since weight quantization is much more mature and easier to optimize than activation quantization, shifting the quantization difficulty from activations to weights leads to much better overall INT8 inference accuracy without changing the model's computation.

At this point, you've covered the three major conceptual milestones in post-training quantization:

GPTQ — second-order error compensation.
AWQ — activation-aware protection of important weight channels.
SmoothQuant — activation-aware redistribution of quantization difficulty from activations to weights.

These form the conceptual backbone of modern LLM quantization.

- SmoothQuant "stores one scale per channel."

## More precisely:

The channel scaling factors S used to redistribute difficulty between activations and weights are computed once from calibration and baked into the transformed model.
During activation quantization itself, the runtime quantizer may still use the associated quantization parameters (scale, and possibly zero-point depending on symmetric/asymmetric quantization). The important conceptual point is that the redistribution scaling is fixed after calibration, not recomputed for every prompt.

This distinction becomes important later when we study dynamic quantization methods.
