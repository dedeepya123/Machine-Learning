## KV Cache Mental Model

What is stored?

For every token:

At every layer:

Store:

K
V

These are needed by future tokens during attention.

---

KV Cache is stored:

Per Layer

Layer1 KV Cache
Layer2 KV Cache
...
LayerN KV Cache

Each layer has its own representations.

---

Memory Formula:

Memory =

2 × Layers × KV_Heads × Head_Dim × Context_Length × Bytes

where:

2 = K and V

Bytes = datatype size (FP16 = 2 bytes)

---

Memory grows linearly with:

* Context length
* Number of layers
* Number of KV heads

---

FlashAttention:

Reduces attention computation cost.

Does NOT reduce KV cache size.

---

PagedAttention:

Improves KV cache allocation and fragmentation.

Does NOT reduce KV cache size.

---

MQA:

Reduces KV heads dramatically.

Directly reduces KV cache memory.

---

GQA:

Uses a small number of KV heads.

Balances quality and memory.

---

Key Insight:

In modern LLM inference, KV cache is often one of the largest memory consumers.
