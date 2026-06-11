## Why was Top-k Sampling introduced?

Problem With Sampling:

Sampling preserves diversity but can occasionally choose very low-probability tokens.

These tokens often lead to:

* Nonsensical outputs
* Hallucinations
* Unstable generation

Researcher Insight:

The model already indicates which tokens are unlikely.

Why not remove them before sampling?

Idea:

Sort tokens by probability.

Keep only the top k tokens.

Discard all others.

Then renormalize probabilities and sample.

This method is called:

Top-k Sampling

Example:

k = 3

Keep:

Paris
London
Rome

Discard:

Berlin
Pizza
Dinosaur

Benefits:

* More diverse than Greedy Decoding
* Less random than pure Sampling
* Reduces low-quality token selection

Deep Intuition:

Sampling:

Everyone enters the lottery.

Top-k:

Only the finalists enter the lottery.

Problem Researchers Found:

Top-k uses a fixed number of tokens.

But model confidence changes from step to step.

Sometimes 1 token is enough.

Sometimes 20 tokens are reasonable.

A fixed k cannot adapt to confidence.

This led to the next idea: Top-p (Nucleus) Sampling.

## summary

Top-k Sampling keeps only the k highest-probability tokens predicted by the model, discards all others, renormalizes the remaining probabilities, and samples from this reduced distribution.

It reduces the chance of selecting very low-probability tokens while still maintaining diversity through sampling.
