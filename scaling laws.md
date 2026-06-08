Scaling laws emerged from the question:

"How does performance change as we increase model size, data, and compute?"

Researchers measured language modeling loss because it is the fundamental training objective of language models.

They discovered that loss decreases smoothly and predictably as model size, dataset size, and compute increase.

This was surprising because neural networks were expected to behave in a more chaotic and unpredictable way.

The key insight was that larger models consistently learn better representations.

Scaling laws suggested that capabilities might continue improving simply by increasing scale, without requiring major architectural changes.

This shifted the research mindset from:

"New capabilities require new architectures"

toward:

"New capabilities may emerge from scale itself."

This idea became the foundation for GPT-3.

Scaling laws are empirical relationships showing how language-model performance (usually training/validation loss) changes as model size, dataset size, and compute are increased.

The key discovery was:

Loss decreases predictably
as scale increases.

Researchers found that:

Parameters ↑
Data ↑
Compute ↑
↓
Loss ↓

following smooth mathematical curves.

The important part is not the exact equation.

The important part is:

Performance did not saturate unexpectedly. It improved in a predictable way.

This gave researchers confidence that building larger models would continue yielding improvements.

Researchers trained:

Small models
Medium models
Large models

with varying:

Parameter counts
Dataset sizes
Training budgets

and measured losses.

For example (conceptually):

100M params
300M params
1B params
3B params

and plotted:

Parameter Count
vs
Validation Loss

Then they noticed:

The points weren't random.

They almost formed a smooth curve.

Like:

*
  *
    *
      *
         *

This was the discovery.

Why Was It Worth Spending So Much?

Because once the curve exists, you can estimate:

If I train a 10× larger model,
what loss might I get?

without actually training hundreds of giant models.

Think of it like physics.

If I know:

distance = speed × time

I don't need to physically drive every route.

I can predict.

Scaling laws gave researchers that predictive power.

What Is This Alpha (α)?

Excellent.

Let's look carefully.

Researchers observed relationships like:

Loss∝N
−α

where:

N = number of parameters

and

α (alpha)

is just a fitted constant.

Think:

Loss=
N
α
1
	​


(up to constants)

Alpha tells:

How fast loss improves as model size grows.

Example:

If

α=1

then doubling parameters gives a large improvement.

If

α=0.01

then doubling parameters barely helps.

Researchers found real values somewhere in between.

The exact number is less important than the interpretation:

Alpha = rate of improvement

The contribution was:

Researchers discovered that language-model improvement follows surprisingly regular mathematical trends.

That led to the mindset:

Maybe we can predict capability growth.

And that mindset directly motivated GPT-3.

Scaling laws showed that validation loss decreases predictably as model size, dataset size, and compute increase.

Researchers derived these laws by training many models of different scales and fitting mathematical curves to the results.

The exponent α determines how quickly performance improves with scale and reflects diminishing returns.

The key insight was that larger models continued improving in a smooth, predictable way, suggesting that scaling itself could be a major driver of capability.
