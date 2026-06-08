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
