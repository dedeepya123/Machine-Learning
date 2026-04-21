# Regularization → L2 (Ridge)
## 1. Where we are coming from
We trained models by minimizing data error:
Loss = difference between predicted and actual values
using gradient descent, weights were updated iteratively.
## 2. Problem observed
* Model fits training data well
* But fails on unseen data
Overfitting
## 3. Why overfitting happens
* Data contains noise
* Some datapoints produce large errors
* These create strong gradients
Across iterations:
* gradients for some parameters keep pointing in same direction
* updates accumulate
weights grow large
## 4. Why large weights are a problem
* Large weights → small change in input causes large change in output
* Model becomes sensitive / unstable
* Fits noise instead of true pattern
High variance → Overfitting
## 5. Key realization
> Error is not only about fitting data
> Model complexity (sensitivity) also matters
## 6. Idea of Regularization
> Control model complexity while fitting data
We modify objective:
Loss = data loss + penalty on weights
## 7. L2 Regularization (Ridge)
Penalty term:
Full objective:
## 8. Why square of weights?
* penalizes large weights more strongly
* smooth and differentiable
* gives stable optimization
## 9. Effect on Gradient
## 10. Update rule
## 11. What happens in each iteration
Each step has two effects:
### Data term
* pushes weights to reduce error
### Regularization term
* shrinks weights toward zero
 push + pull
## 12. Connection to accumulation
Without regularization:
* gradients accumulate
* weights grow large
With L2:
* each step shrinks weights
* accumulation is controlled
## 13. Why weights don’t go to zero
Because:
* data term keeps pushing weights
* regularization pulls them back
final weights are a balance:
## 14. Effect on model
* weights stay small
* function becomes smoother
* less sensitive to noise
reduced variance
## 15. Bias–Variance tradeoff
* increasing λ:
  * ↓ variance
  * ↑ bias
λ controls tradeoff
## 16. Final intuition
> L2 regularization adds a force that continuously pulls weights toward zero, preventing them from growing large due to accumulated gradients,resulting in a simpler and more generalizable model.
## 17. One-line takeaway
> L2 regularization reduces overfitting by penalizing large weights and shrinking them during every update step.
