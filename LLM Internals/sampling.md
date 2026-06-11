## If Greedy Decoding is repetitive and boring, what was the next idea researchers tried?

Observation:

The model does not directly output a word.

It outputs a probability distribution over the vocabulary.

Example:

Paris = 0.72

London = 0.15

Rome = 0.08

Berlin = 0.04

Pizza = 0.01

Researcher Insight:

Greedy Decoding throws away almost all information in the distribution and keeps only the highest-probability token.

Instead, why not use the distribution itself?

Idea:

Randomly sample a token according to the probabilities predicted by the model.

This is called:

Sampling (Multinomial Sampling)

Benefits:

* More diverse outputs
* More natural text
* Less repetition
* Better creative generation

New Problem:

Sampling can occasionally choose low-probability tokens.

This can introduce:

* Nonsensical outputs
* Hallucinations
* Unstable generation

Deep Insight:

Researchers discovered a tradeoff:

Greedy Decoding:

* Safe
* Deterministic
* Repetitive

Sampling:

* Diverse
* Creative
* Potentially noisy
## Summary 
Sampling is a decoding strategy where the next token is randomly selected according to the probability distribution produced by the model, rather than always choosing the highest-probability token.

This preserves the uncertainty represented by the model and produces more diverse outputs, but may also introduce errors and randomness.
