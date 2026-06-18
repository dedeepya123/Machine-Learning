Memory Systems - Clarifications

What is a Memory System?

A memory system is any mechanism that:

* Stores information
* Updates information
* Retrieves information

Memory system does not necessarily mean database or retrieval system.

It is a broader concept.

---

Examples of Memory Systems

1. Internal Memory Systems

Examples:

* RNN
* LSTM
* Transformer-XL
* Recurrent Transformers

Memory lives inside model computation.

---

2. External Memory Systems

Examples:

* ChatGPT Memory
* Agent Memory
* Company Knowledge Stores
* Personal Assistant Memory

Memory lives outside model weights.

---

3. Hybrid Systems

Most modern architectures.

Weights
+
External Memory

---

Who Decides Internal vs External?

Case 1:

Pretraining

Researchers decide.

Internet data is compressed into model weights.

Becomes internal memory.

---

Case 2:

Application-Level Memory

Application logic decides what gets stored externally.

Example:

User preferences.

---

Case 3:

LLM-Assisted Memory Formation

Model evaluates whether information is important.

System stores selected memories.

---

Key Insight:

Internal and External Memory are not competitors.

They solve different problems.

---

Internal Memory:

Slow-changing knowledge.

Examples:

Language

Reasoning

General world knowledge

---

External Memory:

Fast-changing knowledge.

Examples:

User preferences

Recent events

Documents

Conversation history

---

Pretraining creates internal memory.

Inference-time systems create external memory.

This separation led to the development of modern memory systems research.
