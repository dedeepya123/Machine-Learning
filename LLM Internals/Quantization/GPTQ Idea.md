GPTQ does not change
the quantization formula.

Normal quantization is still used.

--------------------------------

Weight Error

E = Wq - W

--------------------------------

Layer Output

Y = WX

--------------------------------

Output Error

Yq - Y

=

EX

--------------------------------

Key Insight

Network cares about
output error

not raw weight error.

--------------------------------

Goal

Minimize

||EX||

instead of

||E||

--------------------------------

Compensation Idea

Quantize one column.

↓

Creates output error.

↓

Modify remaining
unquantized columns.

↓

Reduce output error.

--------------------------------

Inspired by OBS

but applied locally
inside a layer.

--------------------------------

Sequential Strategy

Quantize

↓

Compensate

↓

Quantize

↓

Compensate

↓

Repeat

--------------------------------

This becomes GPTQ.
