# EAGLE (Extrapolation Algorithm for Greater LLM Efficiency)
1. Motivation

After understanding Speculative Decoding and Medusa, researchers noticed an important observation.

Both methods accelerate inference by drafting future tokens and letting the large model verify them.

However:

Speculative Decoding requires an entire second draft model.
Medusa requires training several extra token prediction heads on the large model.

Researchers asked:

Can we speculate future tokens without using another model and without predicting tokens directly?

This led to EAGLE.

2. Key Insight

Instead of predicting future tokens, EAGLE predicts future hidden representations (features).

Why?

Because hidden representations evolve much more smoothly than discrete tokens.

Consider

The capital of France is

At this point, the transformer's hidden state already contains:

France
Capital
Geography
Paris is highly likely

The next hidden representation is therefore largely determined.

Predicting

Current Feature
↓

Future Feature

is easier than predicting

Current Tokens
↓

Next Token
3. Core Idea

Instead of

Prompt
↓

Transformer
↓

Next Token

EAGLE performs

Prompt
↓

Transformer
↓

Current Hidden Feature

↓

Predict Future Hidden Feature

↓

LM Head

↓

Draft Token

The expensive transformer is executed only occasionally.

The lightweight predictor generates speculative future hidden states.

4. Training

The original transformer is completely frozen.

<img width="1172" height="705" alt="image" src="https://github.com/user-attachments/assets/12de4d67-330e-47d1-ab9f-0e990dc9e310" />

<img width="1132" height="682" alt="image" src="https://github.com/user-attachments/assets/032efca6-ee31-49f4-b843-aa78593b497e" />

<img width="1052" height="562" alt="image" src="https://github.com/user-attachments/assets/9e3b6294-a003-4b3c-b5fc-b77960600dfe" />

<img width="1187" height="597" alt="image" src="https://github.com/user-attachments/assets/e1af5a85-7e3d-4905-a6fb-8f52e0adf5c3" />

<img width="757" height="277" alt="image" src="https://github.com/user-attachments/assets/b91a5477-756a-451d-9d3c-723dc1e213aa" />


6. Predictor Network

The predictor is intentionally very lightweight.

Researchers do not use another transformer.

Otherwise,

we would simply recreate Speculative Decoding with another model.

Instead,

the predictor learns

Conceptually

Current Feature

+

Predicted Token Information

↓

Residual Update

↓

Future Feature

<img width="1077" height="437" alt="image" src="https://github.com/user-attachments/assets/d9c43f5b-3156-4ee7-b6e7-4c0f673f8766" />

<img width="1236" height="657" alt="image" src="https://github.com/user-attachments/assets/2fac4b94-5a3e-4a07-86f0-af396b0ee933" />

<img width="1235" height="730" alt="image" src="https://github.com/user-attachments/assets/13cb37dc-66e4-439e-9ecf-3f23425a2c23" />

<img width="1156" height="167" alt="image" src="https://github.com/user-attachments/assets/6ba755a2-848c-475a-85e6-b89c444a0cc2" />

Repeat recursively.

h_t

↓

ĥ₁

↓

Paris

↓

ĥ₂

↓

.

↓

ĥ₃

↓

...

Thus the predictor drafts several future tokens without repeatedly executing the transformer.

8. Why Doesn't Recursive Prediction Drift Forever?

Recursive prediction naturally accumulates error.

Training always sees

true hidden states.

Inference sees

predicted hidden states.

This is similar to exposure bias in sequence models.

Small prediction errors accumulate.

EAGLE handles this in two ways.

Short speculative windows

Only predict a few future steps

typically

3–5.

Transformer verification

Exactly like Speculative Decoding,

the drafted sequence is verified by the original transformer.

Transformer

↓

Predict 4 Features

↓

Draft Tokens

↓

Transformer Verification

↓

Accept Longest Correct Prefix

↓

Repeat

Every verification resets accumulated error.

Therefore,

prediction never drifts very far.

9. Why Is EAGLE Faster?

Normal decoding

Token 1

↓

Transformer

↓

Token 2

↓

Transformer

↓

Token 3

↓

Transformer

One transformer pass per token.

EAGLE

Transformer

↓

Predict 4 Future Features

↓

Draft 4 Tokens

↓

Single Verification Pass

↓

Accept Multiple Tokens

Many tokens are accepted after only one expensive transformer execution.

<img width="1266" height="307" alt="image" src="https://github.com/user-attachments/assets/a0a6f801-c38e-42e7-9bd7-33d41f50a70d" />

11. Why Is EAGLE Different from Medusa?

Medusa predicts

Future Tokens

directly.

EAGLE predicts

Future Hidden Representations

first,

then converts them into tokens using the existing LM head.

Researchers found hidden representations evolve much more smoothly than discrete tokens, making them easier to extrapolate accurately.

# summary 

EAGLE accelerates autoregressive decoding by learning to predict future transformer hidden representations instead of future tokens. A lightweight predictor is trained on hidden-state transitions while the original transformer remains frozen. During inference, the predictor recursively extrapolates several future hidden states, converts them into draft tokens using the existing LM head, and the original transformer verifies the drafted sequence. Since hidden representations evolve more smoothly than discrete tokens, feature prediction is easier than token prediction, enabling faster inference without requiring a separate draft model.


Speculative Decoding:
"Use a small LLM to guess future tokens."

↓

Medusa:
"Use extra token heads on the same LLM to guess future tokens."

↓

EAGLE:
"Don't guess tokens directly—predict where the transformer's hidden representation will move next, then decode tokens from those predicted features."










Only the predictor network is trained.

