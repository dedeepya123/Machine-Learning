Why Prompting Works and What In-Context Learning Really Means
1. The Initial Surprise

GPT is trained using only one objective:

P(x
t
	​

∣x
<t
	​

)

i.e.

Predict the next token.

During training, the model is never explicitly told:

Translate text
Answer questions
Write code
Summarize documents

Yet after training, it can perform all of these tasks.

The natural question is:

How can a model trained only for next-token prediction perform so many different tasks?

2. What Pretraining Actually Learns

A common misconception is:

Next-token prediction
=
Learning to predict words

In reality:

Next-token prediction
=
Training signal

while the model actually learns:

Grammar
Syntax
Semantics
Facts
Reasoning patterns
Programming patterns
Dialogue structures
Task formats

because understanding these helps reduce prediction loss.

Analogy with CNNs

CNN objective:

Dog vs Cat classification

But CNN internally learns:

Edges
Textures
Shapes
Objects

These representations become reusable for many vision tasks.

Similarly:

GPT objective:

Next-token prediction

But GPT internally learns:

Language structure
Knowledge
Reasoning patterns
Task structures

which become reusable across many NLP tasks.

3. What Emerges During Pretraining

Very roughly:

Embeddings
↓
Word identity
↓
Local grammatical patterns
↓
Sentence structure
↓
Semantic meaning
↓
Entity relationships
↓
Knowledge representations
↓
Prediction-oriented representations

Just as CNNs learn:

Pixels
↓
Edges
↓
Textures
↓
Objects

Transformers learn increasingly abstract language representations.

4. Attention, FFNs and Residual Stream
Attention

Attention primarily learns:

Information routing

It determines:

Which tokens should exchange information.

Examples:

Subject ↔ Verb
Pronoun ↔ Entity
Opening bracket ↔ Closing bracket
Previous occurrence ↔ Current occurrence
FFNs

FFNs primarily learn:

Feature formation
Knowledge transformations
Concept activation

A useful intuition:

Attention = Communication

FFN = Memory + Computation
Residual Stream

The residual stream acts as:

Shared information highway

Each block:

Reads from residual stream
↓
Computes something useful
↓
Writes back to residual stream

Over many layers, richer information accumulates.

5. Why Prompting Works

A prompt is simply text.

Example:

Translate to French:

I love machine learning.

To humans this looks like an instruction.

To GPT it is simply another sequence of tokens.

However, during pretraining the model has seen many patterns similar to:

Instruction → Completion

Question → Answer

English → French

Problem → Solution

As a result, the prompt activates representations associated with those patterns.

Important

Prompting does NOT change weights.

Weights remain fixed.

Only activations change.

Think:

Weights
=
Long-term memory

Prompt
=
Current context

Activations
=
Current computation
6. What Are Activations?

During the forward pass every layer computes vectors.

Example:

Token: house

Layer 10 representation:

[0.23, -1.18, 0.71, ...]

These vectors are activations.

They:

Exist temporarily
Influence computation
Disappear after inference

Unlike weights, they are not stored permanently.

7. What Is In-Context Learning?

Traditional learning:

Experience
↓
Weight update
↓
New behavior

In-context learning:

Examples in prompt
↓
Activation changes
↓
New behavior

No weight updates occur.

Example:

dog → chien

cat → chat

house →

Model outputs:

maison

without any retraining.

This phenomenon is called:

In-Context Learning

because the model appears to adapt using only information present in the context window.

8. Is The Model Really Learning?

This is still an active research question.

What we know:

Not traditional learning

During inference:

No gradient descent
No backpropagation
No parameter updates

Therefore:

No new knowledge is permanently stored.
What likely happens

Pretraining teaches:

Translation patterns
QA patterns
Reasoning patterns
Programming patterns
Pattern-recognition strategies

Prompt examples activate these existing capabilities.

Thus the model is often:

Recognizing
Selecting
Combining
Applying

previously learned patterns.

9. Mechanistic View of In-Context Learning

Consider:

dog → chien

cat → chat

house →

When predicting after:

house →

attention can look at:

dog → chien

cat → chat

and detect:

Input → Output mapping pattern

Information from those examples flows through:

Attention
↓
Residual Stream
↓
Later Layers

and influences the prediction.

The model may infer:

Current task = Translation

and then retrieve:

house ↔ maison

from knowledge already learned during pretraining.

10. Induction Heads

Researchers discovered special attention heads called:

Induction Heads

They learn patterns like:

If sequence A appeared before,
look at what followed A.

Example:

Alice likes apples.

Bob likes bananas.

Alice likes

The head can:

Find previous occurrence
↓
Attend to following token
↓
Reuse information

These heads are believed to be an important mechanism behind in-context learning.

Final Mental Model
Pretraining
↓
Learns knowledge, language structure,
reasoning patterns, task formats

Weights
↓
Store long-term capabilities

Prompt
↓
Provides current task information

Attention
↓
Uses prompt context to retrieve relevant information

Residual Stream
↓
Acts as temporary workspace

Activations
↓
Store task-specific computation

Generation
↓
Produces output using capabilities learned during pretraining

Pretraining learns the capabilities; prompting and in-context learning dynamically select and apply those capabilities using temporary activations, without changing the model's weights.
