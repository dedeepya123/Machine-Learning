## MQA reduces KV cache dramatically but loses some quality.Can we find a middle ground?

---

MHA:

Each head has:

Q_i, K_i, V_i

Pros:

* Maximum expressiveness

Cons:

* Large KV cache

---

MQA:

Many Query heads.

One shared K head.
One shared V head.

Pros:

* Very small KV cache

Cons:

* Reduced expressiveness

---

GQA Idea:

Group Query heads.

Example:

Q1-Q4 → K1,V1

Q5-Q8 → K2,V2

...

Each group shares K/V.

---

Benefits:

* Much smaller KV cache than MHA
* Much better quality than MQA

---

Memory Example:

32 Query Heads

MHA:

32 KV heads

MQA:

1 KV head

GQA:

8 KV heads

Memory reduction:

32/8 = 4× compared to MHA

---

Deep Insight:

Not every attention head needs a unique K/V representation.

A small number of shared K/V groups captures most of the benefit.

---

Evolution:

MHA
→ MQA
→ GQA

GQA became the practical solution used in many modern LLMs.
