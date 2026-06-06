A single Transformer block does not learn language understanding in one step.

Each block performs two operations:

1. Attention:

   * Exchanges information between tokens.
   * Builds richer contextual representations.

2. FFN:

   * Computes higher-level features from those contextual representations.

When blocks are stacked, each layer receives increasingly richer representations from the previous layer.

Early layers tend to learn local lexical and syntactic patterns.

Middle layers learn relationships, dependencies, and structure.

Later layers learn semantic concepts, reasoning patterns, and task-relevant abstractions.

Language understanding emerges gradually through repeated cycles of communication (attention) and computation (FFN).
