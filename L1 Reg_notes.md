# Regularization → L1 (Lasso)

## 1. Where we are coming from
During training:
* gradients from datapoints accumulate
* some weights grow large (fit strong patterns)
* some weights remain small (weak / noisy features)
## 2. Problem
* Model starts using even weak features
* tries to fit noise
* increases complexity
Overfitting
## 3. Key observation
Not all features are equally useful:
* some → strong, consistent signal
* some → weak / inconsistent
We want:
> keep important features, remove unnecessary ones
## 4. Idea of L1 Regularization
Add penalty on absolute value of weights: J(w)=g_data + lambda*abs(w)
## 5. Why absolute value?
* applies **same penalty regardless of weight size**
* creates a **constant pull toward zero**
## 6. Gradient of L1
Total gradient:
## 7. Update rule
## 8. Effect of update
* if (w_j > 0) → decreases
* if (w_j < 0) → increases
always moves **toward zero**
## 9. Key mechanism (very important)
Compare:
* data gradient (g_{\text{data}})
* regularization strength (\lambda)
### Cases
g_data<lambda
regularization dominates
weight keeps shrinking
eventually: Wt --> 0
## 10. Why some weights become zero
Because:
* weak features → small data gradients
* L1 adds constant push
L1 overpowers weak signals
eliminates those weights
## 11. What happens at zero
* derivative is not smooth
* subgradient allows weight to stay at 0
 once zero → tends to remain zero
## 12. Why overfitting connects here
* overfitting uses many weak patterns
* L1 removes weak contributors
reduces complexity by reducing number of features
## 13. Meaning of small data gradient
Small gradient means:
* error is small
  OR
* feature values are small
  OR
* contributions cancel out
  OR
* feature is not consistently useful
weak influence on prediction
## 14. Final effect of L1
* many weights = 0
* few important weights remain
* simpler model
sparse model
## 15. Comparison with L2

| L2                 | L1               |   |   |
| ------------------ | ---------------- | - | - |
| penalty = (w^2)    | penalty = (      | w | ) |
| smooth shrink      | constant push    |   |   |
| weights → small    | weights → zero   |   |   |
| keeps all features | selects features |   |   |

## 16. Final intuition
> L1 regularization applies a constant force that removes weak features by driving their weights to zero, keeping only the most important features in the model.
> L1 performs feature selection by eliminating weights whose contribution is not strong enough to overcome the regularization penalty.
