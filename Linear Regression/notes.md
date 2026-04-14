# Simple Linear Regression

## Problem
- Given input data where each data point has a single feature, we want to find the relationship between input and output.
## Model Assumption
  We assume a linear relationship: Y=mX+b
## Goal
- Find the best parameter (m,b) such that predictions are close to actual values.
## How do we measure “good”?
- We define a Loss Function:
    Error=actual-predicted
    Loss=mean of (error^2)
## How do we find best parameters?
- We use optimization.
   Instead of trying all values, we Iteratively update parameters to reduce loss.
## How do we update parameters
- We use an optimization algorithm (Gradient Descent)
- Compute gradient of loss w.r.t parameters
- Gradient tells:
      direction to move
      how sensitive loss is to parameter change
Each data point:
- produces an error
- contributes to how parameters should change
All contributions combine → gradient
## Update Rule
new_param=old_param-learning_rate*gradient
We repeat until: 
- loss is minimized or convergence is reached

# Extension to Multiple Regression
## Problem:
- Now each data point has multiple features: x = [x₁, x₂, x₃, …]
We want to learn a relationship between these features and output.
## Model Assumption (Extended)
- We assume linear relationship again: y = w₁x₁ + w₂x₂ + … + wₙxₙ + b
- Each feature has its own weight
- Weigh=importance of that feature
## Dataset Representation
X → (num_samples,num_features)
Y → (num_samples)
## Goal 
- same as before
Find best weights (w₁,w₂, …) and bias (b) that minimize loss.
## Training Process
For each iteration (epoch):
- Compute predictions
- Compute error
- Compute loss (mean squared error)
- Compute gradients (for each weight)
- Update parameters
## Note
- Each data point influences parameter updates based on:
  its error, its feature values
- Gradient=combined effect of all data points
## Final Understanding
- Model=weighted sum of features
- Loss=how wrong we are
- Gradient=how to fix it
- Training=iterative optimization

