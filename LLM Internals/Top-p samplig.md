## Why was Top-p Sampling introduced?

Problem With Top-k:

Top-k keeps a fixed number of tokens.

But model confidence changes at every generation step.

Examples:

High confidence:

Paris = 0.95

London = 0.02

Rome = 0.01

Only a few tokens matter.

Low confidence:

Many tokens have similar probabilities.

Many alternatives are reasonable.

A fixed k cannot adapt to both situations.

Researcher Insight:

Instead of keeping a fixed number of tokens,

keep enough tokens to cover most of the model's belief.

Idea:

Sort tokens by probability.

Compute cumulative probability.

Keep the smallest set of tokens whose cumulative probability exceeds threshold p.

Example:

p = 0.95

Keep:

Paris
London
Rome

Discard:

Berlin
Pizza

This method is called:

Top-p Sampling

or

Nucleus Sampling

Why "Nucleus"?

Because it keeps only the nucleus of the probability distribution that contains most of the probability mass.

Deep Intuition:

Top-k:

Keep a fixed number of candidates.

Top-p:

Keep enough candidates to explain most of the model's belief.

Benefits:

* Adapts to confidence automatically
* Better diversity
* More stable generation
* Reduces unlikely token selection

Modern LLMs commonly use:

Temperature + Top-p Sampling

Next Research Question:

All current methods choose one token at a time.

Can a slightly worse token now lead to a much better sequence later?

This question led to Beam Search.


## Summary 

Top-p (Nucleus Sampling) keeps the smallest set of highest-probability tokens whose cumulative probability exceeds a threshold p, then renormalizes and samples from that set.

Unlike Top-k, it dynamically adapts the number of candidate tokens based on the model's confidence.
