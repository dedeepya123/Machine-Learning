Problem

Quantizing a weight
introduces error.

--------------------------------

Research Question

Is the damage permanent?

Or can other weights help?

--------------------------------

Observation

Weights are not independent.

Many weight configurations
can produce similar outputs.

--------------------------------

Example

w₁ decreases

↓

w₂ increases

↓

Output remains similar.

--------------------------------

Meaning

Neural networks contain
redundancy.

--------------------------------

Hessian Interpretation

Diagonal:

Sensitivity of individual weight.

Off-diagonal:

Interaction between weights.

--------------------------------

Large H₁₂

=

Changing w₁ can be partially
compensated by changing w₂.

--------------------------------

Small H₁₂

=

Weights behave independently.

--------------------------------

New Idea

Instead of preventing error,

allow error

and compensate elsewhere.

--------------------------------

Birth of

Error Compensation
