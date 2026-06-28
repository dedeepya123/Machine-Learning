# Speculative Decoding

## 1. Motivation
Why do we need Speculative Decoding?

During autoregressive inference, an LLM generates one token at a time.

For each token:

Current Context
       │
       ▼
Large LLM Forward Pass
       │
       ▼
Next Token
       │
       ▼
Append Token
       │
       ▼
Repeat

Even though GPUs parallelize computation within one forward pass, they cannot parallelize across future tokens because each token depends on the previous one.

If we generate 100 tokens:

100 Sequential Large Model Forward Passes

This sequential dependency becomes the main inference bottleneck.

## 2. First Idea

Researchers asked:

Instead of making the expensive model generate every token, can a much smaller model generate several tokens first?

Example

Prompt

↓

Small Model

Paris
.
<eos>

↓

Large Model

The intuition was:

Small model is much faster.
Large model is much more accurate.

<img width="1106" height="660" alt="image" src="https://github.com/user-attachments/assets/66c0c26a-f92d-4254-bed7-994ddd1bb9df" />

## 4. Key Observation

Transformers already process entire sequences during training.

Example

The capital of France is Paris .

A single forward pass produces

Position 1 → Predict capital

Position 2 → Predict of

Position 3 → Predict France

Position 4 → Predict is

Position 5 → Predict Paris

Position 6 → Predict .

because causal masking allows every position to predict its next token simultaneously.

Researchers realized:

If the draft model proposes several tokens, the target model can evaluate all drafted positions in one forward pass, exactly like training.

This is the fundamental insight behind Speculative Decoding.

## 5. Overall Algorithm
Prompt
      │
      ▼
Draft Model
Generates k tokens sequentially
      │
      ▼
Append Draft Tokens
      │
      ▼
Target Model
One Forward Pass
      │
      ▼
Produces next-token distribution
for every drafted position
      │
      ▼
Verify draft tokens

<img width="987" height="527" alt="image" src="https://github.com/user-attachments/assets/09d9a2b7-0fd2-4094-bf4f-ffba2fa686a1" />

<img width="912" height="372" alt="image" src="https://github.com/user-attachments/assets/d9f3b144-d442-4857-ad49-afbbbffcb141" />


## 7. Why This Acceptance Rule?

Suppose

Draft proposes

Paris

95%

Target model wants

Paris

80%

If we always accept,

Paris appears

95%

of the time.

Wrong.

Instead,

accept only

0.95 / 0.80
	​
of the Paris proposals.

Then

0.95 × 0.80 / 0.95 = 0.80

Exactly the target probability.

This naturally leads to

A(x)=min(1,q/p)
	​

<img width="1147" height="557" alt="image" src="https://github.com/user-attachments/assets/06f6122a-6aa5-418c-adda-9a44b3010712" />


Intuition

Accepted draft proposals consume part of the target model's probability budget.

Residual sampling distributes whatever probability mass is still missing.

## 9. Why Stop at First Rejection?

Suppose

Draft

Paris
beautiful
city

If

Paris

is rejected,

then

beautiful

was generated assuming

Paris

was correct.

Its context is now invalid.

Therefore
- reject remaining drafted tokens,
- discard them,
- sample one replacement,
- restart drafting from the new context.

<img width="1127" height="627" alt="image" src="https://github.com/user-attachments/assets/84d4e9ae-9272-4830-b77b-bc6d59aeda48" />

<img width="1367" height="677" alt="image" src="https://github.com/user-attachments/assets/6e694389-4124-4734-be49-fdebd575682d" />

Hence Speculative Decoding produces exactly the same distribution as standard autoregressive decoding.

## 11. Why Is It Faster?

Normal decoding

Large Model

↓

Token 1

↓

Large Model

↓

Token 2

↓

Large Model

↓

Token 3

Requires

k expensive forward passes

Speculative Decoding

Small Model

↓

k cheap forward passes

↓

Large Model

↓

1 expensive forward pass

Since the small model is much cheaper, many expensive decoding steps are replaced by inexpensive draft steps, significantly reducing inference latency when the draft is accepted frequently.

## 12. Advantages
- Exact output distribution
- No retraining of the target model
- Significant reduction in decoding latency
- Simple integration with existing autoregressive models

## 13. Limitations
- Requires maintaining two models in memory.
- Speedup depends on how often the draft model agrees with the target model.
- Frequent rejections reduce performance.
- Additional verification logic is required.

## Summary

<img width="1022" height="496" alt="image" src="https://github.com/user-attachments/assets/d9e35e7f-a076-4a5b-88b7-ce4ee26dcaf4" />
