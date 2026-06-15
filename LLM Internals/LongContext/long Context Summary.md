Step 1: What Problem Is RoPE Trying To Solve?

Suppose we have:

I love deep learning

Tokens:

0   1    2     3

Without positions:

deep learning love I

looks identical to the model.

So we need positional information.

Researchers ask:

How do I encode position 0,1,2,3,... ?

Step 2: RoPE's Weird Idea

Instead of creating:

Position 0 → vector A
Position 1 → vector B
Position 2 → vector C

RoPE says:

Let's create many clocks.

Imagine 64 clocks.

(Actually 64 pairs if head_dim=128.)

Clock 1 spins very fast.

Clock 2 spins slightly slower.

Clock 3 slower.

...

Clock 64 extremely slow.

Step 3: Position = Read All Clocks

Suppose:

Position:

p=10

Every clock shows a value.

Clock 1:

3 o'clock

Clock 2:

8 o'clock

Clock 3:

1 o'clock

...

Together:

(3,8,1,...)

uniquely identify position 10.

This is the key idea.

Step 4: Where Do Frequencies Come In?

Each clock spins at a different speed.

Fast clock:

Huge frequency.

Slow clock:

Small frequency.

Mathematically:

θ
i
	​


is simply:

Speed of clock i

Nothing more.

Step 5: What Is Wavelength?

Now let's focus on ONE clock.

Suppose it spins very fast.

Position:

0

clock points:

↑

Position:

8

clock points:

↑

again.

Meaning:

After 8 positions it completed a full rotation.

Then:

λ=8

This wavelength belongs to the clock.

NOT the position.

This is the first confusion you had.

Wavelength is NOT:

Property of position.

It is:

Property of a frequency/clock.
Why Do We Care?

Because wavelength tells us:

What positional distance this clock can distinguish.
Example

Clock A:

λ=8

Very sensitive.

Position:

100

101

102

all look noticeably different.

Useful for nearby tokens.

Another Clock
λ=50000

Position:

100

101

102

almost identical.

No local information.

But:

100

vs

40000

looks different.

Useful for large-scale information.

This Is What Local/Global Means

When people say:

Local frequency

they mean:

Small wavelength clock.

When people say:

Global frequency

they mean:

Large wavelength clock.

Not positions.

Not attention.

The clocks themselves.

Step 6: How Does Position Use All Frequencies?

Suppose:

Head dimension:

128

RoPE creates:

64 clocks.

Position 100 becomes:

Clock1 value
Clock2 value
Clock3 value
...
Clock64 value

Together they form the positional geometry.

Now Q and K get rotated using all these clocks.

Therefore:

Q/K contain:

local information
+
medium information
+
global information

all mixed together.

Step 7: Now Long Context Appears

Training length:

2048

Researchers suddenly want:

128000

Question:

What happens to our clocks?

Look At Fast Clock

Suppose:

λ=8

Within 2048 tokens:

Clock already completed:

2048/8=256

rotations.

Model saw lots of behavior.

Nothing surprising.

Look At Very Slow Clock

Suppose:

λ=50000

Within training:

2048/50000

Almost no movement.

Model only saw tiny part of that clock.

Now inference:

128K context.

Suddenly this clock rotates much more.

Model enters geometry it never trained on.

THIS is the actual problem.

Notice:

The problematic frequencies are usually the very slow ones.

Because training never explored much of their rotation.

This is the piece that is often explained incorrectly online.

Why Compression Helps

Researchers say:

Let's make those huge-scale clocks rotate slower.

Now:

Position 128K

looks more like

Position 2K

geometry.

Distribution shift reduced.

Why Not Compress Everything?

Because fast clocks are already working.

They encode:

token 100
vs
token 101

beautifully.

Compress them too much:

Local precision disappears.

Grammar.

Syntax.

Nearby retrieval.

All degrade.

Hence YaRN.

YaRN's Real Thought Process

Researchers looked at clocks and asked:

Which clocks are already useful?

Keep them.

Which clocks become problematic
when context explodes?

Compress them.

What about middle clocks?

Blend.

That's the whole story.

The Biggest Clarification

You asked:

Which frequencies are problematic?

The answer is:

Not because of attention.

Not because of retrieval.

Not because of positions directly.

They are problematic because:

Their rotational behavior at long context
was never seen during training.
