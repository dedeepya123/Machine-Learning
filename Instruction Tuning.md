## Why was GPT-3 not naturally a good assistant?

GPT-3 was pretrained on next-token prediction. During pretraining it learned many capabilities such as translation, summarization, reasoning, and coding.

However, GPT-3 primarily learned pattern completion rather than instruction following.

As a result, few-shot examples often worked better than natural language instructions because examples explicitly revealed the desired pattern.

Researchers realized that the capabilities already existed inside the model, but the model was not reliably activating them from instructions alone.

Instruction tuning was introduced to solve this problem.

The idea was to train on datasets of:

Instruction
Input
Output

so that the model learns:

Instruction → Task → Desired Behavior

rather than simply continuing text patterns.

A useful mental model is:

Pretraining builds capabilities.
Instruction tuning teaches when and how to use those capabilities.

This is why instruction-tuned models require fewer examples and behave more like assistants.


## Why was instruction tuning needed if GPT-3 already worked in zero-shot settings?

GPT-3 could often understand instructions, but instruction following was inconsistent because pretraining optimized for continuing internet text rather than obeying user requests.

The model possessed many capabilities, but did not reliably activate them from natural language instructions.

Researchers created datasets of:

Instruction
Input
Output

Examples:

Translate → Translation Output
Summarize → Summary
Classify → Label

The training objective remained standard next-token prediction using cross-entropy loss.

Instruction tuning did not primarily create new capabilities. Most capabilities were already learned during pretraining.

Instead, instruction tuning taught the model how to map natural language instructions to the appropriate pretrained capability.

A useful mental model is:

Pretraining = Learning skills

Instruction Tuning = Learning when and how to use those skills

This explains why a relatively small instruction dataset can dramatically improve model behavior.

## Is Instruction Tuning Just Fine-Tuning?

Yes, Technically:

Pretraining
↓
Instruction Tuning

is simply another stage of training.

Or in ML terminology:

Supervised Fine-Tuning (SFT)

on an instruction dataset.

So when people say:

Instruction Tuned Model

under the hood it usually means:

Pretrained Model
+
Supervised Fine-Tuning
on Instruction Data

Large models learned different capabilities but sometimes continued text instead of following instructions.


Imagine GPT-3 sees:

Translate this sentence to French:
I love dogs.

Researchers know:

Translation capability exists.

because few-shot prompting already showed that.

The problem was:

Capability exists
≠
Capability reliably activated

Sometimes GPT-3 might:

Translate

Sometimes:

Continue the document

Sometimes:

Generate unrelated text

Researchers wanted:

Instruction
↓
Desired behavior

to become consistent.

## Who Invented Instruction Tuning?

This is where the history gets interesting.

It was not only OpenAI.

Multiple groups were converging on similar ideas.

Some important milestones:

OpenAI (GPT-3, InstructGPT)
Google Research (FLAN)
DeepMind
Academic researchers

In fact, one of the most influential instruction-tuning papers was:

Finetuned Language Models Are Zero-Shot Learners from Google researchers.

## How Did They Create Instruction Datasets?

This is the next natural question researchers faced.

They thought:

We already have thousands of NLP datasets. Why not convert them into instructions?

For example:

Original sentiment dataset:

Movie review:
Amazing film.

Label:
Positive

Convert to instruction form:

Instruction:
Determine whether the sentiment is positive or negative.

Input:
Amazing film.

Output:
Positive

Same task.

Different formatting.

Another Example

Original translation dataset:

English:
Dog

French:
Chien

Instruction version:

Translate the following word into French.

Dog

Chien

Again, same information.

Now expressed as a natural-language instruction.

Where Did The Data Come From?

Researchers already had:

Translation datasets

QA datasets

Summarization datasets

Classification datasets

Reasoning datasets

They converted them into:

Instruction
Input
Output

triples.

This is why instruction tuning happened surprisingly fast.

The data already existed.

The format changed.

## Why Did Researchers Think This Would Help?

This is the key reasoning.

Researchers had already observed:

Few-shot prompting works.

Meaning:

Capabilities already exist.

Therefore they hypothesized:

Maybe the model doesn't need more knowledge.

Instead it needs:

Better task routing.

This is a huge conceptual shift.

## What Did They Hope To Gain?

Researchers wanted:

Better Zero-Shot

Instead of:

dog -> chien
cat -> chat
house ->

They wanted:

Translate house into French.

to work immediately.

Better Generalization

Not:

One prompt style works.
Another prompt style fails.

But:

Many ways of asking
↓
Same behavior
Better Human Interaction

Humans naturally communicate via instructions.

Explain this.

Summarize this.

Write an email.

Help me debug.

Researchers wanted models to respond to those naturally.

The Deep Mental Model

Think of GPT-3 as:

Huge toolbox

with thousands of tools inside.

Instruction tuning teaches:

When user says X,
use tool Y.

It doesn't build the toolbox.

It organizes access to it.

## summary

GPT-3 demonstrated that many capabilities emerge during pretraining.

However, those capabilities were not always robustly activated by natural language instructions because the model was trained to continue text, not act as a helpful assistant.

Researchers hypothesized that capabilities already existed and that a small amount of supervised fine-tuning on instruction datasets could teach the model how to map instructions to the appropriate behavior.

Instruction tuning therefore focuses more on capability elicitation and task routing than on creating entirely new capabilities.
