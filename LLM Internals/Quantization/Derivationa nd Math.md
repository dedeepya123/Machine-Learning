Quantization Levels

Real weights are continuous.

Example:

0.123451
0.123452
0.123453

Infinite possibilities.

--------------------------------

INT8

Only 256 possible values:

-128 ... 127

These are called:

Quantization Levels

--------------------------------

Idea

Map continuous values
to nearest discrete level.

--------------------------------

Scale

Determines:

How much real-value distance
one integer step represents.

Formula:

scale

=

(real_max - real_min)

/

(int_max - int_min)

--------------------------------

Quantization

q

=

round(w / scale)

--------------------------------

Dequantization

w ≈ q × scale

--------------------------------

Problem

What if real range
is not centered around zero?

Need shift.

--------------------------------

Zero Point

Represents where real zero
lies in integer space.

--------------------------------

Final Formula

q

=

round(w/s)

+

z

Dequantization

w

≈

(q-z)s

--------------------------------

Scale

=

Distance between levels

Zero Point

=

Location of real zero
inside integer levels
