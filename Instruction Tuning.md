Why was GPT-3 not naturally a good assistant?

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
