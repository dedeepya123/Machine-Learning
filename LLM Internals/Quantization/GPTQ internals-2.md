Why Sequential?

Quantizing all columns together
mixes errors.

Hard to compensate.

--------------------------------

GPTQ Strategy

Quantize one column at a time.

--------------------------------

Column i

↓

Quantize

qi = Quantize(wi)

--------------------------------

Error

ei = qi - wi

--------------------------------

Error measured immediately
after quantizing the column.

--------------------------------

Compensation

Uses H⁻¹

to distribute error into
remaining FP columns.

--------------------------------

Interpretation

Column i of H⁻¹

tells how strongly other
columns interact with
column i.

--------------------------------

Large interaction

↓

More compensation.

--------------------------------

Already quantized columns

↓

Frozen.

Never changed again.

--------------------------------

Remaining FP columns

↓

Receive compensation.

--------------------------------

When quantizing column 2

Use compensated

w₂(new)

not original w₂.

--------------------------------

Loop

Quantize

↓

Error

↓

Compensate

↓

Update remaining columns

↓

Next column
