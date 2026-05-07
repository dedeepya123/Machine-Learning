## Why do Decision Trees overfit so easily?

We know trees learn: keep splitting until nodes become pure
If allowed indefinitely, the tree can create rules like:
if age=31 AND salary=10.13L AND city=X ...
 It memorizing training data instead of learning general patterns.

## What actually happens?
Tree keeps reducing impurity:
Gini → smaller and smaller
until eventually: every leaf may contain 1 sample
Then:
- training error ≈ 0
- variance very high
- poor generalization
## Important insight
Unlike linear models: trees have extremely high flexibility
because they can keep partitioning feature space infinitely.

## “When should we STOP splitting?”
- This is the actual regularization problem in trees.
When should a tree stop?
A split should happen only if: the split is meaningfully improving generalization not just memorizing noise.

## Common stopping / regularization methods
### 1. Max Depth
Constraint: maximum levels allowed in tree
Example:
max_depth = 3
After depth 3:
stop splitting

Why this helps
Deep trees: learn highly specific rules
Shallow trees: learn broader patterns

#### Relation to bias-variance
##### Small depth
- higher bias
- lower variance
##### Large depth
- lower bias
- high variance
Exactly same tradeoff again.
### 2. Minimum Samples per Split
Only split if node has enough samples.
Example:
min_samples_split = 10
If node has:
<10 samples don’t split further.

Why? Tiny nodes often represent:
noise or outliers

### 3. Minimum Samples per Leaf
Require each final leaf to contain enough samples.
Example:
min_samples_leaf = 5
This prevent
single-sample memorization
🔹 4. Minimum Information Gain

Split only if impurity reduction is significant.

Example:

IG > threshold

If impurity reduction tiny:

split not worth it
🧠 Beautiful intuition

Tree asks:

“Am I learning a real pattern or just tiny noise?”

🔹 5. Pruning

Very important concept.

Instead of stopping early:

first grow large tree

then:

remove unnecessary branches
🎯 Why pruning works

Some splits improve training accuracy but hurt validation performance.

Pruning removes such branches.

🧠 Two types
Pre-pruning

Stop early while building.

Examples:

max depth
min samples
Post-pruning

Build full tree first, then cut branches.

Usually better.

🎯 BIG conceptual connection

This is exactly analogous to regularization.

Linear Models

Control:

weight magnitudes
Trees

Control:

tree complexity
🧠 Very important interview insight

A Decision Tree does NOT naturally know:

when to stop

Without constraints:

it will keep reducing impurity forever

even fitting noise.

🎯 One-line intuition

Overfitting happens when the tree keeps splitting to memorize tiny details instead of learning general decision rules.

🧠 Final mental picture

Tree growth:

More splits
→ lower impurity
→ more complex rules
→ lower bias
→ higher variance

Regularization/pruning controls this complexity.
