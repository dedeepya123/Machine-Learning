# In-Context Learning (ICL)

## What is In-Context Learning?

In-context learning is the ability of a language model to adapt its behavior using examples provided in the prompt, without updating any model weights.

Example:

dog -> chien

cat -> chat

house -> ?

The model infers the task (English → French translation) from the examples and continues with:

house -> maison

---

## Is the Model Actually Learning?

Not in the traditional sense.

During inference:

* Weights remain fixed
* No gradient descent occurs
* No parameters are updated

Instead:

Prompt
→ Creates activations
→ Activations encode task information
→ Model adapts behavior temporarily

When the prompt changes, those activations disappear.

Thus, in-context learning is temporary adaptation through activations, not permanent learning through weight updates.

---

## Why Does In-Context Learning Work?

During pretraining, the model repeatedly sees patterns such as:

Question → Answer

Example → Solution

English → French

Problem → Explanation

To minimize next-token prediction loss, the model learns to:

1. Detect patterns in context
2. Infer the underlying task
3. Continue the pattern

Therefore, the model learns not only knowledge but also how to use context.

---

## Why Does Few-Shot Prompting Help?

Few-shot prompting provides multiple demonstrations of the desired behavior.

Example:

dog -> chien

cat -> chat

book -> livre

house -> ?

These examples make the task pattern explicit, allowing the model to infer:

English word
↓
French word

and apply it to the new input.

---

## Why Does In-Context Learning Improve With Scale?

Larger models learn richer representations and more sophisticated circuits during pretraining.

As model size increases, the model becomes better at:

* Detecting patterns from examples
* Inferring tasks from context
* Retrieving relevant knowledge
* Applying learned patterns to new inputs

Thus, scale improves not only knowledge but also the ability to learn from the prompt itself.

---

## Key Mental Model

Pretraining teaches:

"What capabilities exist?"

Prompting tells:

"Which capability should be used right now?"

In-context learning is the mechanism that allows the model to infer the current task from examples present in the prompt.

---

## One-Line Summary

In-context learning is the ability of a pretrained language model to temporarily infer and perform a task from examples in the prompt, using activations rather than weight updates.


## Why does few-shot prompting improve with scale?

During pretraining, language models repeatedly encounter patterns where earlier text provides examples and later text follows the same structure.

To reduce next-token prediction loss, the model learns to identify patterns inside the current context and use them when predicting future tokens.

In-context learning is therefore not weight learning. No parameters are updated during inference.

Instead:

Prompt
→ Creates activations
→ Activations encode the inferred task
→ Model applies capabilities learned during pretraining

Larger models possess richer representations and more sophisticated circuits, allowing them to:

1. Detect patterns from examples
2. Infer the underlying task
3. Retrieve relevant knowledge
4. Apply the pattern to new inputs

Thus scaling improves not only knowledge storage but also the ability to learn from context during a single forward pass.

GPT-3 demonstrated that language models can adapt behavior using examples present in the prompt, even when weights remain fixed. This phenomenon became known as in-context learning.
