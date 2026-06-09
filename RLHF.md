## What is RLHF Technically?
RLHF (Reinforcement Learning from Human Feedback) was introduced because instruction tuning alone could not fully capture human preferences.

Many tasks have multiple valid answers, and humans often care about qualities such as helpfulness, clarity, safety, honesty, and organization.

RLHF works in three major steps:

1. Collect Preference Data
   Humans compare multiple model outputs and choose the preferred one.

2. Train a Reward Model
   A neural network learns to predict which outputs humans would prefer.

3. Reinforcement Learning
   The assistant generates answers and receives rewards from the reward model.
   The assistant is then optimized to generate higher-reward responses.

Mental Model:

Pretraining → Learn capabilities

Instruction Tuning → Learn task following

RLHF → Learn human preferences

The combination of these stages transformed GPT-style language models into conversational assistants such as ChatGPT.


## The Story

### The State Before RLHF

We have:

Pretrained GPT
↓
Instruction Tuning
↓
Instruction-following GPT

This model can do:

Translate

Summarize

Code

Answer Questions

But researchers observe:

Not always helpful

Not always conversational

Not always aligned

So the question becomes:

How do we teach "human preferences"?

### First Researcher Insight

Researchers asked:

What are humans actually good at?

Writing perfect answers?

Not always.

Ranking answers?

Very good.

For example:

Prompt:

How should I learn Python?

Answer A

Answer B

Most humans can quickly say:

B is better.

This insight drives everything.

How Is The Preference Dataset Created?

This was your first doubt.

Very important.

Researchers already have:

Instruction Tuned Model

Now they sample outputs from it.

Example:

Prompt:

How should I learn Python?

Run model multiple times.

Maybe get:

Output A
Read documentation.
Output B
Start with basics, build projects...
Output C
Learn syntax then practice...

Now humans compare.

Human says:

B > C > A

Store:

Prompt

Chosen Answer

Rejected Answer

Dataset grows.

Thousands.

Then tens of thousands.

Then hundreds of thousands.

Notice:

The answers came from the instruction-tuned model itself.

Humans are evaluating model outputs.

### What Does The Dataset Look Like?

A single training example:

Prompt:
How do I learn Python?

Chosen:
Start with fundamentals...

Rejected:
Read documentation.

That's it.

Next Step: Reward Model

Now researchers ask:

### Can we train a neural network to imitate human preferences?

The answer is yes.

What Is The Reward Model?

Very important.

It's usually:

Same Transformer Family

as GPT.

Often:

Smaller GPT

or

Copy of GPT

with a different head.

Input:

Prompt + Answer

Output:

Single Number

Example:

Prompt + Answer A
→ 2.3
Prompt + Answer B
→ 8.1

Higher means:

Humans likely prefer this.
### What Does The Reward Model Learn?

Not facts.

Not language.

Not translation.

GPT already learned those.

Reward model learns:

Human Preference Function

Meaning:

Helpfulness

Clarity

Politeness

Safety

Completeness

Organization

as reflected in human rankings.

### How Is The Reward Model Trained?

This is beautiful.

Suppose:

Human says:

Answer B > Answer A

Reward model predicts:

Reward(A) = 6

Reward(B) = 8

Good.

Suppose instead:

Reward(A) = 8

Reward(B) = 5

Bad.

Loss encourages:

Reward(chosen)
>
Reward(rejected)

Conceptually:

Human preferred B

Model should score B higher

That's the whole idea.

### Why Does It Need Large Data?

Exactly your observation.

Humans can prefer outputs from:

Coding

Math

Writing

Reasoning

Summarization

Translation

Conversation

Therefore preference dataset must contain:

Many tasks

Many domains

Many prompts

Otherwise reward model won't generalize.

So yes.

A significant amount of human-labeled preference data is required.

Now Comes The Assistant

This is where many people get confused.

You asked:

### How does instruction-tuned model suddenly become assistant?

Answer:

It doesn't suddenly become one.

It already is the model.

Let's rename things.

Before RLHF:

Instruction-Tuned GPT

Researchers now call it:

Policy Model

or

Assistant Model

It's the same model.

Nothing magical happened.

Why Call It Assistant?

Because now its job is:

Generate responses

which will be judged by the reward model.

So:

Instruction Tuned GPT
=
Initial Assistant
What Happens Next?

Assistant generates:

Response

Reward model scores:

Response
→ Reward

Then RL updates assistant.

Goal:

Generate higher reward answers.

Over many iterations:

Assistant learns:

Humans prefer this style.
