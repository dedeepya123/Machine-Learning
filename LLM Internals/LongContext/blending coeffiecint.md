The blending coefficient αi is ultimately chosen based on the wavelength (or equivalently the frequency) of that RoPE dimension.

But let's make the chain crystal clear:

Step 1

Each RoPE pair has a frequency:

θ
i
	​


From that frequency we compute:

λ
i
	​

=
θ
i
	​

2π
	​


This wavelength tells us:

What positional scale this clock represents.

Small wavelength:

Local scale.

Large wavelength:

Global scale.
Step 2

Researchers decide:

Local scales should be preserved.

Therefore:

α
i
	​

≈0

Meaning:

θ
i
′
	​

=θ
i
	​


No compression.

Step 3

For very large wavelengths:

Researchers decide:

These are the scales that become problematic
at long context.

Therefore:

α
i
	​

≈1

Meaning:

θ
i
′
	​

=
s
θ
i
	​

	​


Full compression.

Step 4

For wavelengths in between:

Researchers gradually increase:

α
i
	​


from

0

to

1

Visually:

Small λ          Large λ

0   0   0.2   0.5   0.8   1   1

This creates the smooth transition.

Another Way To Think About It

YaRN is really doing:

Wavelength
      ↓
Positional Scale
      ↓
How much compression should be applied?
      ↓
Alpha coefficient

Not:

Position
      ↓
Alpha

And not:

Attention score
      ↓
Alpha

The decision is made entirely from the frequency/wavelength structure of RoPE.

Tiny Example

Suppose we have 3 clocks.

Clock A:

λ=8

Very local.

Researchers choose:

α=0

Keep unchanged.

Clock B:

λ=1000

Middle scale.

Researchers choose:

α=0.5

Partially compress.

Clock C:

λ=50000

Very global.

Researchers choose:

α=1

Fully compress.

One Small Refinement

You said:

blending coefficient is decided based on wavelength

✅ Conceptually yes.

More precisely:

Researchers define wavelength thresholds (or equivalent frequency thresholds), and then α
i
	​

 is computed from where that frequency lies relative to those thresholds.

So the actual implementation looks like:

Compute wavelength
↓
Check which region it belongs to
↓
Assign alpha
↓
Blend original and scaled frequency

## One-line summary
Wavelength→Positional Scale→αi
	​

→Amount of Compression
	​
