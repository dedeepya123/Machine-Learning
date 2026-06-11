## Once the model produces a probability distribution over the vocabulary, how do we choose the next token?

First Researcher Idea:

Always choose the token with the highest probability.

Mathematically:

token = argmax(probability)

This method is called:

Greedy Decoding

Why Researchers Liked It:

* Simple
* Fast
* Deterministic
* Easy to implement

Example:

Prompt:

"The capital of France is"

Distribution:

Paris = 0.72

London = 0.15

Rome = 0.08

Greedy chooses:

Paris

Problem Researchers Observed:

For longer generation tasks:

* Repetitive outputs
* Boring responses
* Low diversity
* Error accumulation

Why?

Greedy only optimizes:

Highest probability token at the current step.

It does not consider:

* Alternative continuations
* Diversity
* Creativity
* Future sequence quality

Deep Insight:

The model produces a full probability distribution.

Greedy Decoding throws away almost all information in that distribution and keeps only the single highest-probability token.

This often leads to safe and repetitive generation.

## Summary 

- Greedy Decoding is an inference strategy where, at each generation step, the token with the highest predicted probability is selected:

token=argmax(Pi)

-It is deterministic, fast, and simple, but often produces repetitive and low-diversity text because it optimizes only the immediate next-token probability rather than considering alternative future continuations.
