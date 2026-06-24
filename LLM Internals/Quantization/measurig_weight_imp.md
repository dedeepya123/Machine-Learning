Earlier Goal

Minimize Weight Error

--------------------------------

Researchers Realize

Same weight error

≠

Same model impact

--------------------------------

Example

Weight A

Very important

Weight B

Less important

Same quantization error

Different effect on output.

--------------------------------

New Goal

Minimize Model Output Error

not merely

Minimize Weight Error

--------------------------------

First Idea

Use Gradients

dL/dw

Measures sensitivity.

--------------------------------

Problem

After training,

gradients are often near zero.

Need richer information.

--------------------------------

Second Idea

Look at Curvature.

Wide valley

↓

Weight can move freely.

Sharp valley

↓

Weight must stay precise.

--------------------------------

Birth Of Importance Estimation

Question:

Which weights can tolerate
quantization?

Which weights are critical?

--------------------------------

This becomes the foundation
for advanced quantization
methods.
