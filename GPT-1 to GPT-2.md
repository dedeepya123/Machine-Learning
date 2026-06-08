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

GPT-2 did not introduce a fundamentally new architecture. It remained a decoder-only Transformer trained with next-token prediction.

Its main contribution was testing the scaling hypothesis by increasing model size, training data, and compute.

Researchers expected gradual improvements, but observed stronger capabilities than anticipated.

As scale increased, the model became better not only at storing knowledge but also at using prompts, adapting to examples, and performing tasks without task-specific fine-tuning.

This suggested that many capabilities were emerging directly from pretraining rather than from downstream task training.

GPT-2 shifted the community's perspective from:

"Pretraining helps task learning"

to:

"Pretraining may already be learning much of the task."

Scaling laws showed that increasing parameters, data, and compute leads to predictable improvements in model performance.

Researchers initially expected only gradual benchmark improvements. Instead, larger models displayed qualitatively stronger behaviors such as in-context learning, instruction following, knowledge retrieval, and long-range reasoning.

One explanation is that representations improve continuously, while benchmarks reveal capabilities only after a threshold is crossed.

Another explanation is that larger models can learn new internal algorithms and circuits that smaller models cannot represent effectively.

The key insight from GPT-2 was that many capabilities appear to emerge during pretraining itself, suggesting that scale may be a major driver of intelligence in language models.
