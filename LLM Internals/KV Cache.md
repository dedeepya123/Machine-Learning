## If we only compute Q, K, V for the new token, how does attention work using KV Cache?

Initial Prompt:

Example:

"The capital of France is"

Sequence length = 5

KV Cache:

Initially empty.

Model performs a normal forward pass on all prompt tokens.

For every layer:

Compute:

Q, K, V

Store:

K_cache
V_cache

Important:

Each Transformer layer maintains its own KV Cache.

Generation Step:

Model generates:

"Paris"

Now sequence length becomes 6.

Researcher Insight:

Previous tokens have not changed.

Therefore their:

K vectors
V vectors

are identical to those computed earlier.

No need to recompute them.

Only process the newly generated token.

Input Shape:

Before:

(1, 5, Hidden)

Now:

(1, 1, Hidden)

Compute:

Q_new
K_new
V_new

Append:

K_new → K_cache

V_new → V_cache

Attention Computation:

Q_new attends to:

K_cache + K_new

Result:

New token can access information from all previous tokens.

Deep Intuition:

The new token asks:

"Which previous tokens are important?"

Old tokens do not need to recompute their representations.

Their Keys and Values are already stored in memory.

KV Cache acts like a temporary notebook that stores previous token representations.

Instead of recomputing the entire prompt every generation step, the model only computes representations for the newest token and reuses cached information from earlier tokens.

Benefit:

Massive reduction in inference computation and latency.
