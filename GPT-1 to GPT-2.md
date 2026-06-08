GPT-1 established the pretrain-then-fine-tune paradigm.

However, researchers noticed that pretrained language models already seemed to possess many capabilities before fine-tuning.

This led to a new hypothesis: perhaps pretraining itself is learning much of the knowledge and behavior required for downstream tasks.

GPT-2 was an exploration of this idea through scaling.

Rather than introducing major architectural changes, GPT-2 increased model size, data, and compute to test whether more general capabilities would emerge automatically.

This marked the beginning of the scaling hypothesis:

Same architecture
+ More parameters
+ More data
+ More compute
= More capability

The long-term goal was to move from:

Pretrain → Fine-tune

toward:

Pretrain → Prompt
