## Original Situation
Suppose we have a pretrained model:

Training context = 2048 tokens

During training the model learned:

attention patterns
language structure
reasoning
retrieval

all within roughly:

0→2048

positions.

Then Users Want More

People ask:

Why can't I put a whole book?

Why can't I put a huge codebase?

Why can't I put hundreds of pages?

Researchers now want:

32K
64K
128K
256K
1M

contexts.

Immediate Problem

The model was never trained on:

128000

positions.

So researchers ask:

Can we somehow make a 2K-trained model work at 128K?

Without retraining from scratch.

This is where all the methods appeared.

First Attempt

Use RoPE directly.

Observation:

Technically works.

Quality becomes bad.

Because positional geometry moves outside training distribution.

Then Came
Position Scaling

Make large positions look smaller.

NTK Scaling

Scale frequencies more carefully.

Position Interpolation

Compress positions into training range.

Then fine-tune.

YaRN

Preserve local positional scales.

Compress long-range scales more intelligently.

All trying to answer:

How can a 2K-trained model behave well at 128K?
Important Clarification

The model already knows language.

The model already knows reasoning.

The model already knows attention.

The problem is mostly:

How do we extend positional understanding
to much larger contexts?

Think of it like this.

Suppose you trained a child to navigate a city.

Now suddenly you ask them to navigate an entire country.

The child already knows:

roads
maps
directions

The problem is:

The scale became much larger.

Long-context research is largely solving that scaling problem.

But Eventually Researchers Realized Something

After fixing positional encodings:

You can feed:

128K tokens

But now another problem appears.

Attention cost explodes.

Memory explodes.

Latency explodes.

GPU cost explodes.

Which leads to the next generation of research:

Can we even AFFORD
to process 128K?

That is where:

FlashAttention
Sparse Attention
Sliding Window Attention
Ring Attention
Long-context architectures
State Space Models
Memory systems

start appearing.

The Story So Far

You can think of the journey as:

Chapter 1:
How do models learn?
(Training)

↓

Chapter 2:
How do models generate?
(Inference)

↓

Chapter 3:
How do we serve millions of users?
(Serving Systems)

↓

Chapter 4:
How do we efficiently compute attention?
(FlashAttention)

↓

Chapter 5:
How do we extend context length?
(RoPE → NTK → PI → YaRN)

↓

Chapter 6:
How do we afford huge contexts?
(Long Context Efficiency)

And yes, everything from RoPE scaling, Position Interpolation, NTK Scaling, and YaRN is fundamentally part of the research effort:

"Take a model trained on ~2K context and make it reliably understand, retrieve from, and reason over 32K/128K/1M contexts."
