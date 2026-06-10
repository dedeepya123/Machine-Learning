## If previous tokens never change, can't we save their Key and Value vectors and reuse them instead of recomputing them every generation step?

Researcher Observation:

During inference, model generates one token at a time.

Example:

Prompt:

I love deep learning because

Model generates:

it

Now sequence becomes:

I love deep learning because it

To generate the next token, GPT receives the entire sequence again.

Problem:

For every generation step, the model recomputes:

Q, K, V

for all previous tokens.

But previous tokens have not changed.

Their:

* embeddings
* model weights
* computations

are exactly the same.

Therefore:

Old K and V vectors are identical to those computed in the previous generation step.

Researcher Insight:

Instead of recomputing old K and V vectors:

Store them once.

Reuse them later.

This stored memory is called:

KV Cache

Why Cache K and V?

For a new token:

We need:

Q_new

because the new token is asking:

"Which previous tokens should I attend to?"

But old:

K_old
V_old

never change.

So:

Compute only:

Q_new
K_new
V_new

Append:

K_new
V_new

to cache.

Reuse:

K_old
V_old

from cache.

Deep Intuition:

Without KV Cache:

Every generation step recomputes information from all previous tokens.

With KV Cache:

Previous computations are remembered.

Only the newly generated token requires fresh computation.

Analogy:

Without KV Cache:

Rewrite the entire notebook after every new sentence.

With KV Cache:

Keep the notebook and append one new line.

Result:

Much faster inference and significantly lower computation.
