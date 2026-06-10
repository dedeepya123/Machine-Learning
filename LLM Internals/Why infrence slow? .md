## If KV Cache exists, why is inference still slower than training?

Researcher Observation:

Training processes entire sequences simultaneously.

Example:

"The cat sat on the mat"

All tokens are already known.

Targets:

T → cat

cat → sat

sat → on

...

Because the full sequence exists, the Transformer can compute predictions for all positions in one forward pass.

This allows massive GPU parallelism.

Inference Is Different:

Example Prompt:

"The capital of France is"

Future tokens do not exist yet.

The model must first generate:

Paris

Only then can it generate the next token.

Each new token depends on previously generated tokens.

This creates a dependency chain:

Token t

↓

Token t+1

↓

Token t+2

↓

Token t+3

Generation is inherently sequential.

Role of KV Cache:

KV Cache removes redundant recomputation of previous token Keys and Values.

It makes each generation step cheaper.

However:

KV Cache does NOT remove the sequential dependency between generated tokens.

The model still must generate one token before generating the next.

Deep Intuition:

Training knows the future and can learn from all positions simultaneously.

Inference does not know the future and must create it one token at a time.

This autoregressive dependency is the fundamental bottleneck of LLM inference.
