We want neural networks to learn stable and meaningful representations across all layers.

But even before training starts, poor initialization itself can make the network unstable.

## If all weights are initialized equally:
- neurons remain symmetric
- all neurons learn identical patterns
- representation diversity is lost

So weights must be initialized randomly to break symmetry.

However, purely random initialization also creates problems.

## If weights are too small:

- activations shrink across layers
- gradients become weak
- vanishing gradients occur

## If weights are too large:

- activations explode or saturate
- gradients become unstable or explode

Therefore, initialization must preserve stable propagation across deep layers.

## Mathematical Goal

The actual goal is:
- variance of activations and gradients should remain stable across layers

Weights are chosen carefully so that:
- forward activations maintain stable variance
- backward gradients maintain stable variance through depth.

Intution

Each layer performs: z=Wx+b

If many random inputs and weights combine: variance can grow or shrink layer after layer.

Deep networks amplify this exponentially.

So initialization scales weights according to:
number of input connections sometimes output connections to preserve stable signal magnitude statistically

## Initilzation Variants
### Xavier Initialization

Designed mainly for:
- sigmoid
- tanh
Weights scaled roughly by: 1 / n_in or 2 / (n_in + n_out)

### He Initilazation
Designed for ReLU: Since ReLU suppresses about half activations: 2 / n_in works better for maintaing stable variance.
