We built neural networks that can:

learn representations
propagate gradients stably
generalize better

using:

initialization
BN
residuals
regularization

Now another question appears:

“How should the network actually update its parameters during learning?”

Because:

learning quality depends heavily on updates
gradients alone are not enough
🧠 Step 2 — Basic Gradient Descent

Originally we had:

W=W−η∇
W
	​

L

Meaning:

compute gradient
move opposite direction
reduce loss
🎯 Interpretation

Gradient tells:

how changing weights changes loss

So optimizer uses gradient to:

adjust pattern detectors/representations
🧠 But deep learning optimization became hard

Deep networks have:

millions/billions of parameters
noisy minibatch gradients
curved optimization surfaces
unstable directions
sparse updates

Simple GD became inefficient.

🎯 Therefore optimizers answer:
“How should gradients be used intelligently?”

not merely:

“follow gradient blindly”
🧠 Step 3 — SGD (Stochastic Gradient Descent)

Instead of full dataset:

we use:

small minibatches

Why?

Because full gradient:

expensive
slow
memory heavy

So each batch gives:

approximate noisy direction
🎯 Update becomes

W=W−η∇
W
	​

L
batch
	​


🧠 Beautiful intuition

Each minibatch says:

“adjust representations slightly this way”

Different batches:

slightly different gradients
slightly different opinions

Together optimization gradually learns:

shared useful representations
🧠 Step 4 — Problem with plain SGD

SGD works…

BUT optimization landscape is difficult.

🎯 Imagine loss surface

Some directions:

steep
noisy

Some:

flat
slow

SGD may:

oscillate
zig-zag
move slowly
get unstable
🧠 Representation interpretation

Pattern detectors may:

update inconsistently
overreact to noisy batches
learn slowly

Optimization inefficient.

🎯 Therefore we need smarter updates

This leads to:

Momentum
RMSProp
Adam

Each tries to improve:

how representations are updated during learning
🧠 Step 5 — Momentum intuition

Suppose gradients repeatedly point similar direction.

Plain SGD:

forgets previous movement each step

Momentum says:

“accumulate useful movement history”
🎯 Like rolling ball intuition

Instead of:

small noisy jumps

Momentum builds:

velocity through important directions
🧠 Mathematical idea

Velocity:

v
t
	​

=βv
t−1
	​

+(1−β)∇
W
	​

L

Update:

W=W−ηv
t
	​


🎯 Meaning

Optimizer now uses:

current gradient
past gradient trends

So representation updates become:

smoother and more stable
Why this helps

Momentum:

reduces oscillation
accelerates useful directions
stabilizes noisy updates

So pattern detectors evolve:

more consistently
🎯 Beautiful high-level interpretation

Optimization is no longer:

reacting to single batch gradients

Instead:

tracking long-term learning direction
