## Memory Systems - Part 2

### Memory Representation

Core Question:

Once something is considered important,

what exactly should be stored?

---

Key Insight:

Memory is not storage.

Storage keeps everything.

Memory keeps what matters.

---

Memory Representation Problem:

Experience
↓
Compression
↓
Memory

What format should this compression produce?

---

Option 1: Raw Text

Store:

"Alice lives in Paris"

Advantages:

* No information loss
* Human readable
* Easy to inspect

Problems:

* Large storage
* Memory becomes another huge context
* Hard to scale

---

Option 2: Structured Facts

Store:

Alice
↓
LivesIn
↓
Paris

Advantages:

* Compact
* Easy updates
* Easy reasoning

Problems:

* Loses details
* Requires information extraction

---

Option 3: Hidden-State Memory

Store Transformer hidden representations.

Advantages:

* Already computed
* Contains semantic information
* Easy for model to consume

Problems:

* Hard for humans to interpret
* Context dependent
* Not stable facts

---

Option 4: Summaries

Store compressed natural language summaries.

Advantages:

* Compact
* Human readable
* Preserves important information

Problems:

* Some information loss
* Quality depends on summary

---

Fundamental Tradeoff:

Compression
vs
Fidelity

More Compression:
Less Storage
Less Detail

More Fidelity:
More Detail
More Storage

---

There is no perfect memory representation.

Different systems choose different tradeoffs.

---

Main Insight:

Raw Text = Maximum Detail

Structured Facts = Maximum Compression

Hidden States = Maximum Model Compatibility

Summaries = Balanced Tradeoff

---

Researchers eventually realized that memory representation depends on how the memory will be used later.
