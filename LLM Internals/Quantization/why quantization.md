Why Quantization Exists

FP16 uses:

16 bits per weight

7B model:

≈14GB

Researchers ask:

Do we need all this precision?

--------------------------------

Observation

Neural networks tolerate
small numerical errors.

0.126731

and

0.125

often behave almost identically.

--------------------------------

Idea

Store approximate values
instead of exact values.

--------------------------------

INT8

Stores:

-128 ... 127

256 possible levels

Only 8 bits per weight.

--------------------------------

Memory

FP16:

16 bits

INT8:

8 bits

Memory reduced by 2×.

--------------------------------

Key Insight

Weights are not stored exactly.

They are mapped to nearby
integer levels.

This process is called:

Quantization

because continuous values
become discrete levels.
