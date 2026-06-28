# Medusa: Accelerating LLM Inference Without a Separate Draft Model

## 1. Motivation

We previously studied **Speculative Decoding**, where a small draft model proposes several future tokens and the large model verifies them.

Although this provides significant speedup, it introduces several practical issues:

* We need to maintain two models in GPU memory.
* Every target model requires its own compatible draft model.
* The draft model must be trained or distilled.
* Updating the target model often requires retraining the draft model.
* Deployment becomes more complicated.

Researchers therefore asked a natural question:

> **Can the large model itself generate speculative tokens, eliminating the need for a separate draft model?**

This question led to **Medusa**.

---

# 2. Core Observation

Consider a transformer.

```
Prompt
   │
Transformer Layers
   │
Final Hidden State (h)
   │
LM Head
   │
Next Token
```

The expensive part is the transformer computation.

The final LM head is simply one linear projection

[
\text{logits}=W_{LM}h
]

where

* (h) = final hidden representation
* (W_{LM}) = vocabulary projection matrix.

The transformer has already produced a rich semantic representation of the prompt.

Researchers asked:

> **Why use this representation to predict only one token?**

Perhaps the same hidden representation already contains enough information to make good guesses about several future tokens.

---

# 3. Main Idea

Instead of attaching one LM head,

attach multiple lightweight prediction heads.

```
               Hidden State h
                     │
      ┌────────┬────────┬────────┐
      ▼        ▼        ▼        ▼
    Head1    Head2    Head3    Head4
      │        │        │        │
     t+1      t+2      t+3      t+4
```

Each head predicts a different future position.

Notice:

* The transformer still runs only once.
* Only a few small linear layers are added.
* These additional layers are called **Medusa Heads**.

---

# 4. Training

## Important Clarification

Medusa training **still uses teacher forcing**, exactly like standard LLM training.

The transformer is frozen.

Only the Medusa heads are trained.

---

## Training Example

Sentence

```
Yesterday I forgot my umbrella because it started raining.
```

Suppose the current hidden state corresponds to

```
Yesterday I forgot
```

The future tokens already exist in the dataset.

```
my
umbrella
because
it
```

Instead of supervising only one next token,

different heads receive different targets.

```
Head1 → my

Head2 → umbrella

Head3 → because

Head4 → it
```

---

## Training Objective

Each head has its own parameters

[
W_1,;W_2,;W_3,\dots
]

Each head minimizes its own cross entropy.

For Head (k)

[
L_k
===

CE(\hat y_k,;y_{t+k})
]

Total loss

[
L
=

\sum_{k=1}^{K}
L_k
===

\sum_{k=1}^{K}
CE(\hat y_k,;y_{t+k})
]

Only the Medusa heads receive gradients.

The transformer remains frozen.

---

# 5. Why Don't All Heads Learn the Same Thing?

Every head receives the same hidden representation,

but each head has

* different parameters
* different supervision
* different gradients.

Therefore

Head1 specializes in predicting (t+1),

Head2 specializes in predicting (t+2),

Head3 specializes in predicting (t+3),

and so on.

---

# 6. Inference

Suppose the prompt is

```
The capital of France is
```

After one transformer forward pass,

the heads might produce

```
Head1

Paris
London

-------------------

Head2

.
is

-------------------

Head3

<eos>
beautiful
```

These are **not a coherent sequence**.

They are only independent speculative guesses.

---

# 7. Why Not Simply Concatenate Them?

Head2 never saw

```
Paris
```

It only saw the current hidden state.

Likewise Head3 never saw

```
Paris .
```

Therefore

```
Paris
.
<eos>
```

cannot automatically be trusted.

The predictions must first be verified.

---

# 8. Candidate Tree

Instead of considering only one continuation,

Medusa builds a small candidate tree.

Conceptually

```
                Prompt

              /        \

          Paris      London

          /    \

         .      is
```

The tree stores several possible continuations.

It is **not** an execution tree.

It is simply a compact representation of multiple candidate prefixes.

---

# 9. Why Not Enumerate Every Combination?

If every head predicts

(k)

tokens,

and there are

(m)

heads,

then a full Cartesian product produces

[
k^m
]

candidate sequences.

This quickly becomes impossible.

Therefore

Medusa keeps only a small predefined set of promising branches.

---

# 10. Verification

The transformer is still the final authority.

The Medusa heads merely propose candidates.

During verification

the candidate tree is processed through the transformer.

The transformer computes the true logits.

Only prefixes that remain consistent with the transformer's own decoding are accepted.

The longest valid prefix is appended to the output.

The remaining branches are discarded.

---

# 11. How Can One Forward Pass Verify an Entire Tree?

A transformer accepts only linear sequences.

Medusa therefore **flattens the tree** into candidate branches.

Instead of recomputing the prompt repeatedly,

the prompt's KV cache is reused.

Only speculative tokens require new computation.

To prevent unrelated branches from attending to one another,

Medusa replaces the standard causal attention mask with a **Tree Attention Mask**.

Each speculative token attends only to

* the prompt
* its own ancestors

and never to tokens from different branches.

Thus many candidate branches can be verified in one transformer forward pass.

---

# 12. Complete Inference Pipeline

```
Prompt

↓

Transformer

↓

Hidden State

↓

Multiple Medusa Heads

↓

Top-k Candidate Tokens

↓

Candidate Tree Construction

↓

Tree Attention Mask

↓

One Verification Forward Pass

↓

Accept Longest Valid Prefix

↓

Append Tokens

↓

Repeat
```

---

# 13. Mathematical Summary

Transformer

[
h=f_\theta(x)
]

Medusa heads

[
\hat y_k
========

W_kh
]

Training

[
L
=

\sum_{k=1}^{K}
CE(\hat y_k,;y_{t+k})
]

Inference

* Heads generate speculative future-token candidates.
* Candidates form a tree.
* Tree is verified by the transformer using a tree attention mask.
* Longest valid prefix is accepted.

---

# 14. Advantages

* No separate draft model.
* Only lightweight prediction heads are added.
* Transformer weights remain unchanged.
* Significant decoding acceleration.
* No model distillation required.
* Reuses the same transformer representation efficiently.

---

# 15. Limitations

The Medusa heads predict future tokens directly from the current hidden state.

They never observe the actual intermediate generated tokens.

Therefore predictions become less accurate as the prediction horizon increases.

Adding too many heads eventually reduces acceptance rates because farther future predictions become increasingly uncertain.

---

# Summary (60 seconds)

"Medusa is a speculative decoding technique that removes the need for a separate draft model. Instead of using another network, it attaches several lightweight prediction heads to the frozen transformer's final hidden state. Each head is trained with teacher forcing to predict a different future position, using a summed cross-entropy objective. During inference, these heads propose multiple speculative future tokens, which are organized into a candidate tree. The transformer then verifies all candidate branches simultaneously using a tree attention mask while reusing the prompt KV cache. The transformer's own predictions determine the longest valid prefix to accept. This accelerates decoding while avoiding the deployment complexity of maintaining two separate models."
