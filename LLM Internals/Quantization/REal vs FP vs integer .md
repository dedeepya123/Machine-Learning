Real Number

0.126731

is a mathematical value.

--------------------------------

Floating Point

One representation.

Stores:

Sign
Exponent
Mantissa

Examples:

FP32
FP16
BF16

--------------------------------

Quantization

Stores an approximation
using integers.

Examples:

INT8

-128 ... 127

--------------------------------

Stored Quantized Value

Must be integer.

Examples:

64
-25
127

Cannot be:

64.5
12.3

--------------------------------

Where Did The Decimal Go?

Into the Scale.

Example:

Stored Integer = 64

Scale = 0.00784

Recovered Value

=

64 × 0.00784

=

0.50176

--------------------------------

Quantized Models Usually Store

INT Weights

+

Floating Point Scales

--------------------------------

Main Idea

FP16 stores the actual value.

INT8 stores a bucket index.

Scale tells us what that bucket means.
