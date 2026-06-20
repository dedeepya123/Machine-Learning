Why Floating Point Exists

Computers store bits.

Need a way to represent:

0.126731
12345
0.00012

efficiently.

--------------------------------

Scientific Notation Idea

123000

=

1.23 × 10^5

Store:

Significant Part
+
Scale

--------------------------------

Floating Point

Stores:

Sign
Exponent
Mantissa

Conceptually:

Number

=

Sign × Mantissa × Scale

--------------------------------

FP32

32 bits

1 bit  → Sign

8 bits → Exponent

23 bits → Mantissa

High precision.

Used heavily during training.

--------------------------------

FP16

16 bits

Half the memory.

Example:

7B model

FP32 ≈ 28GB

FP16 ≈ 14GB

--------------------------------

Key Observation

FP16 often performs nearly as well as FP32.

Why?

Neural networks are robust to small numerical errors.

--------------------------------

Researchers Realize

If FP16 works...

Can we use:

INT8?

INT4?

Even fewer bits?

This question leads directly to Quantization.
