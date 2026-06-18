Memory Systems - Part 4

Internal vs External Memory

Core Question:

Where should memory live?

Inside the model?

Or outside the model?

---

Internal Memory

Information stored in model weights.

Example:

Internet
↓
Training
↓
Weights

Knowledge becomes encoded in parameters.

---

Examples:

Language

Facts

Reasoning Patterns

World Knowledge

---

Advantages:

Very fast

No retrieval required

Always available during inference

---

Disadvantages:

Hard to update

Hard to correct

Requires retraining or editing

Limited capacity

---

External Memory

Information stored outside model weights.

Examples:

User Preferences

Conversation History

Documents

Company Knowledge

Agent State

---

Advantages:

Easy to update

Easy to delete

Scales to huge amounts of information

Supports dynamic knowledge

---

Disadvantages:

Requires retrieval

Additional latency

More system complexity

---

Key Insight:

Some information changes too frequently to live inside model weights.

Example:

User preferences

Recent events

Company documents

---

Researchers realized:

Internal Memory

=

General knowledge and reasoning

External Memory

=

Dynamic and personalized information

---

Modern AI systems use both.

Weights
+
External Memory

---

Connection To Long Context Research:

Long-context methods try to keep more information inside the Transformer.

Memory systems ask:

Can important information live outside the Transformer instead?

---

Main Insight:

The best systems combine internal memory (weights) and external memory (memory stores) rather than choosing one.
