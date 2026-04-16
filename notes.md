# Logistic Regression – Notes

## 1. Problem

We want to classify data into 2 classes (0 or 1)
Linear Regression:
* gives continuous values (−∞to+∞)
* not suitable for classification

## 2. First Idea(Threshold)
if (w·x + b ≥ k) → 1
else → 0
Problem:
* not continuous
* not differentiable
* gradient = 0
→ cannot learn using gradient descent

## 3. Solution: Sigmoid Function
We need a function that:
* converts real values to (0,1)
* is continuous
* is differentiable
Sigmoid:
ŷ = 1 / (1 + e^(−z))
where z = w·x + b

## 4. Model
z = w·x + b
ŷ = sigmoid(z)
ŷ = probability that y = 1
To get class:
* if ŷ ≥ 0.5 → 1
* else → 0
## 5. Why not MSE?
We can use:
Loss = (y − ŷ)²
But problem:
* sigmoid becomes flat at extremes (0 or 1)
* gradient becomes very small
* even if prediction is very wrong → update is small
→ slow or bad learning
## 6. Better Loss
Instead of:
“how far is prediction from actual”
Think:
“how much probability we gave to correct class”
## 7. Build Loss
If y = 1:
Loss = −log(ŷ)
If y = 0:
Loss = −log(1 − ŷ)
## 8. Combined Loss (Cross-Entropy)
Loss = − [ y log(ŷ) + (1 − y) log(1 − ŷ) ]
## 9. Intuition of Loss

* ŷ close to correct value → small loss
* ŷ far from correct value → large loss
Example:
* y = 1, ŷ = 0.9 → small loss
* y = 1, ŷ = 0.1 → large loss

## 10. Why log?

* log(1) = 0 → no loss
* log(small value) → large negative
After negative sign:
* correct → small loss
* wrong → large loss

## 11. Gradient
Final result:
∂L/∂w = (ŷ − y) · x

## 12. Training Steps
For each iteration:
1. Compute z = w·x + b
2. Compute ŷ = sigmoid(z)
3. Compute loss
4. Compute gradient
5. Update weights
Update rule:
w = w − lr * gradient

## 13. Key Points
* Logistic Regression = linear model + sigmoid
* Output is probability
* Use cross-entropy loss
* Gradient = (ŷ − y)
## 14. Common Confusions
* Output is not class, it is probability
* MSE fails due to small gradients
* log is used to penalize wrong predictions strongly
* (1 − y) selects class 0 case

---
