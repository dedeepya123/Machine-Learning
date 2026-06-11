## Why was Beam Search introduced?

Problem:

Greedy Decoding and Sampling make irreversible decisions one token at a time.

Once a token is chosen, all alternative futures are discarded.

Researcher Insight:

Instead of keeping one candidate sequence, keep multiple candidate sequences alive simultaneously.

Idea:

Maintain B candidate sequences (beam width).

At each generation step:

1. Expand all candidate sequences.
2. Score all continuations.
3. Keep the best B sequences.
4. Repeat.

This method is called:

Beam Search

Scoring:

Beam Search optimizes sequence probability:

P(sequence)

or equivalently:

Sum of log probabilities.

Deep Difference:

Greedy:

Optimizes next-token probability.

Beam Search:

Optimizes entire sequence probability.

Why It Worked Well:

Tasks such as:

* Machine Translation
* Summarization
* Structured Generation

need accurate high-probability outputs.

Beam Search often improves quality.

Problem Researchers Found:

Highest probability sequence is not always the most natural or interesting sequence.

For open-ended generation:

* Stories
* Conversation
* Creative Writing

Beam Search often produces repetitive and boring outputs.

Historical Lesson:

Better likelihood optimization does not always produce better human-preferred text.

Why Modern Chat Models Prefer:

Temperature + Top-p

instead of Beam Search:

They preserve diversity and naturalness.

Next Research Question:

Everything so far assumes one user.

How do modern systems efficiently serve thousands of users simultaneously?

This leads to LLM Serving Systems.
