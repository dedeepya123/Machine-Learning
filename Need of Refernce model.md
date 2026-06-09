## If GPT outputs are stochastic, and the instruction-tuned model itself can generate many different answers, 
## how can we compare the assistant against the reference model?

We are not comparing the final generated text.

We are comparing the probability distributions of the two models.

This distinction is crucial.

The Wrong Mental Model

Many people imagine:

Reference:
Answer A

Assistant:
Answer B

and then compare:

A vs B

That is NOT what KL penalty does.

Because as you correctly noticed:

GPT can generate many valid answers.

Even the same model can produce:

Run 1:
Learn Python through projects.

Run 2:
Start with fundamentals and practice.

Run 3:
Use online courses and build apps.

All reasonable.

What Is Actually Compared?

Suppose prompt is:

How do I learn Python?

Assistant generates:

Start with basics and build projects.

Now we ask BOTH models:

How likely was this exact sequence according to you?

Reference model says:

Probability = 0.01

Assistant says:

Probability = 0.012

Pretty close.

Good.

KL penalty is small.

What KL Is Really Measuring

Very roughly:

KL(π
assistant
	​

∣∣π
reference
	​

)

measures:

How different are the probability distributions?

Not:

Are the outputs identical?

Huge difference.

Think About A Dice

Suppose Reference Model behaves like:

Token A = 40%

Token B = 30%

Token C = 30%

Assistant behaves like:

Token A = 45%

Token B = 28%

Token C = 27%

Very similar.

KL small.

Now imagine:

Token A = 99.9%

Everything else = 0.1%

KL becomes huge.

Because behavior changed dramatically.

Why This Solves Your Concern

You said:

Same prompt can generate different answers.

Correct.

Researchers know this.

They are NOT trying to force:

Same answer

They are trying to prevent:

Same model becoming
a completely different model.
Example

Instruction tuned model might assign:

Helpful answer = 30%

Another helpful answer = 25%

Another helpful answer = 20%

After RLHF:

Helpful answer = 40%

Better organized answer = 35%

Other answer = 10%

This is fine.

But we don't want:

One weird answer = 99.99%

or

Always generate 5000 words

or

Always say:
"As an AI assistant..."

Those are reward-hacking behaviors.

Another Deep Insight

Reference model is not saying:

This answer is correct.

Reward model already handles:

Human preference.

Reference model says:

Don't move too far
from the language behavior
you originally learned.

Think of it as:

Anchor

not

Teacher
Analogy

Imagine a student.

Original student:

Knows math

Knows physics

Knows programming

You want:

More polite
More helpful

Reward model:

Humans prefer this behavior.

Reference model:

Don't forget everything else
while becoming polite.

That's all.

One Tiny Technical Detail

In practice RLHF often computes something like:

Reward=RewardModelScore−βKL

Interpretation:

High human preference
=
good

Large deviation from reference
=
bad

The assistant seeks balance.

The Mental Model To Keep

If someone asks:

Why is the reference model needed?

Don't think:

Compare outputs.

Think:

Compare probability distributions.

The reference model is not checking:

Did you generate the same answer?

It is checking:

Are your probabilities drifting too far
from the original instruction-tuned GPT?
