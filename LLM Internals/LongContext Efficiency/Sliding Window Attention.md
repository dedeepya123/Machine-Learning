Sliding Window Attention

Problem:

Full attention = O(N²)

For long context this becomes extremely expensive.

---

Observation:

Most information is local.

Current token usually depends on nearby words/sentences.

---

Idea:

Instead of attending to all previous tokens,

attend only to nearby tokens.

---

Window Size:

w

Token i attends only to:

[i-w+1 ... i]

---

Attention Complexity:

Full Attention:

O(N²)

---

Sliding Window:

O(N × w)

---

Example:

N = 100000

w = 512

Full Attention:

10 billion interactions

---

Sliding Window:

51 million interactions

Huge reduction.

---

Benefits:

* Linear scaling
* Much cheaper
* Good local reasoning
* Good grammar/syntax

---

Limitation:

Long-range communication is lost.

Token 100000 cannot directly access token 1.

---

Tradeoff:

Efficiency ↑

Long-range retrieval ↓

---

Key Insight:

Most dependencies are local,
but some important dependencies are global.

This motivates Sparse Attention.

Next Question:

Can we keep mostly local attention while adding a few long-range connections?
