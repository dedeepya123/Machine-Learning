Reward Model
teaches
what humans prefer

PPO
is the optimization algorithm
used to update the Assistant
using those preferences
while keeping updates stable

So PPO itself doesn't know:

Helpful

Honest

Conversational

The Reward Model knows that.

PPO simply says:

Use the reward signal
to improve the assistant
but don't change too aggressively.

## Are we training a new assistant model? Or are we updating the instruction tuned model itself?
Let's see exactly what happens.

After Instruction Tuning

Suppose we have:

Instruction Tuned Model

Parameters: θ
Imagine:

7 Billion weights

for simplicity.

RLHF Starts

Researchers make TWO COPIES.

Instruction Tuned Model
↓
Copy A
Copy B

Copy A

Reference Model

Frozen.

Never updated.

Copy B

Assistant Model
(or Policy Model)

Trainable.

Initially:

Reference == Assistant

exactly.

Same weights.

## Why Need Reference Model?

Researchers need something to compare against.

Remember:

KL penalty.

We want:

Current Assistant

to stay reasonably close to:

Original Instruction Model

But if original model keeps changing:

No stable baseline exists.

Therefore:

Reference Model
=
Frozen Snapshot
What Actually Gets Updated?

Only:

Assistant Model

All Transformer weights.

Everything.

Exactly like normal training.

Example:

Layer 1 weights

Updated

Layer 15 weights

Updated

Layer 40 weights

Updated

Attention matrices.

FFNs.

Embeddings.

Everything.

So yes:

RLHF updates the actual GPT weights.
Visual Picture

Initially:

Reference Model
=
Instruction Tuned GPT

Assistant Model
=
Instruction Tuned GPT

After many PPO updates:

Reference Model
(stays unchanged)

Assistant Model
(becomes more aligned)

Now:

Assistant ≠ Reference

but not too different because of KL penalty.

## Why Not Train Directly From Reference?

Because then KL becomes impossible.

You need:

Original Behavior

available throughout training.

Reference acts like an anchor.

## Deep Intuition

Think of a student.

Original instruction tuned model:

Knows language

Knows reasoning

Knows coding

Researchers say:

Become more helpful.

Instead of replacing the student:

We keep the student.

And continue teaching.

The student's brain changes.

But we keep:

A photograph
of the old student.

That photograph is:

Reference Model

We periodically compare:

Current Student
vs
Old Student

and prevent huge deviations.

One More Important Detail

Many people imagine:

Instruction Model
+
Extra RLHF Layers

No.

Not usually.

Same Transformer.

Same architecture.

Same parameters.

Only:

Weights get updated further.

Exactly like:

Pretraining
↓
Update weights

Instruction Tuning
↓
Update weights

RLHF
↓
Update weights

Same network.

Different objectives.

## Clean Mental Model
Pretraining
creates GPT

Instruction Tuning
modifies GPT

RLHF
further modifies GPT

At each stage:

Same model

New objective

More weight updates

The only special thing during RLHF is:

Frozen Reward Model

Frozen Reference Model

Trainable Assistant Model

## summary:

Reference Model:
Frozen copy of instruction-tuned GPT.
Used only for KL comparison.

Reward Model:
Frozen model that predicts human preference scores.

Assistant Model:
Trainable copy of instruction-tuned GPT.
Updated using PPO to maximize reward while staying close to the reference model.

All weight updates during RLHF happen only inside the Assistant Model.

This clarification is important because once you understand it, the entire RLHF pipeline becomes just another training stage on top of GPT rather than some mysterious separate system.
