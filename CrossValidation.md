## Why do we need Cross Validation?
When we split data into: Train → Validation → Test
Problem:
- performance depends on one validation split and that split may be lucky or unlucky
- So model evaluation becomes unreliable.
Solution
- Cross Validation evaluates the model across multiple train-validation splits instead of relying on a single split.

2. What does Cross Validation do?
- splits data into multiple folds
- trains and validates multiple times
- averages performance
This gives:
- more reliable estimate of model performance
3. What CV actually measures
  - It measures how stable the model performance is across different data splits.
If performance is:
  - consistent → good generalization
  - highly varying → unstable model
4. Role of Cross Validation
- does NOT reduce overfitting directly
- helps detect and avoid overfitting
- helps select best hyperparameters
5. Relation with Regularization
- Regularization → controls model complexity
- Cross Validation → evaluates model properly
Connection:
- CV is used to choose best regularization strength (λ)
 6. Hyperparameter tuning using CV
  * For each hyperparameter (e.g., λ):
  * run CV
  * compute average performance
  * select best value
Also consider: high mean + low variance across folds = best choice
7. Types of Cross Validation
* K-Fold
- split into K equal parts
- train on K-1, validate on 1
- repeat K times
* Stratified K-Fold
- maintains class distribution in each fold
-  Used for classification (especially imbalanced data)
* Leave-One-Out (LOOCV)
  - each sample is a validation set once
  - Useful for very small datasets
  -  computationally expensive
8. When to use what
- Classification → Stratified K-Fold
- Regression → K-Fold
- Very small data → LOOCV
 9. Key Thing
- Cross Validation improves reliability of model evaluation and helps in selecting the best model configuration.
- CV does NOT replace regularization CV helps choose how much regularization to apply
 

