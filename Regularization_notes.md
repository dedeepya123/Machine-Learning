# Regularization 

## 1. Where we came from
We trained models by minimizing error:
Loss = difference between predicted and actual values
Using gradient descent, we updated parameters to reduce this error.
## 2. Problem we observed
* Model fits training data very well
* But fails on unseen data
Overfitting
## 3. Why overfitting happens
* Data contains noise
* Model tries to reduce error for all datapoints
* Some datapoints (noisy ones) produce strong gradients
Over iterations:
* gradients accumulate
* some weights keep increasing
Large weights ⇒ high sensitivity ⇒ unstable function ⇒ high variance
## 4. Key realization
> Error is not only due to how well we fit data
> It is also due to how complex / sensitive the model is
## 5. What causes model complexity?
* More features / transformations
* Large weights (very important)
## 6. Idea of Regularization
> Instead of only minimizing data error, we also control model complexity
## 7. How do we do that?
We modify the objective:
Loss = data error + penalty on weights
## 8. Meaning
* Data error → fit the data
* Penalty → keep weights small
## 9. Why penalize weights?
Because:
* large weights → sharp changes
* sharp changes → fit noise
* fit noise → overfitting
## 10. Final intuition
> Regularization prevents the model from becoming too sensitive by discouraging large weights, helping it focus on the true pattern instead of noise.
> Regularization reduces overfitting by controlling model complexity through penalizing large parameter values.

---
