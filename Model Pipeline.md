End to End Model Pipleine
1. Problem Setup
Given:
- X → input features (N, D)
- y → target values (N,) or (N,1)
Goal:
    Learn model parameters that map X → y
3. Data Preparation
 1. Shuffle data
 2. Split into:
    Train set
    Validation set
    Test set
3. Define Model
Choose model:
    Linear / Logistic / Softmax / etc.
Model form:
    z = XW + b
    y_pred = activation(z)   (if required)
4. Initialize Parameters
W = zeros or small random values
b = 0
Hyperparameters:
    learning_rate
    epochs
    regularization strength (λ)
5. Training Loop
For each epoch:
    1. Forward Pass
        z = X_train @ W + b
        y_pred = model_output(z)
    2. Compute Loss
        data_loss = loss(y_pred, y_train)
        reg_loss = λ * regularization(W)
        total_loss = data_loss + reg_loss
    3. Compute Gradients
        error = y_pred - y_train
        dW = gradient wrt W
        db = gradient wrt b
    4. Update Parameters
        W = W - lr * dW
        b = b - lr * db
    5. Validation (optional but recommended)
        compute val_loss using X_val
6. Convergence Check (optional)
Stop if:
    loss stops decreasing
    OR epochs completed
7. Final Evaluation
Use test set:
    Linear → MSE
    Classification → Accuracy / Precision / Recall / F1
8. Prediction Function
predict(X):
    z = X @ W + b
    return processed output
9. (Optional) Hyperparameter Tuning
For each hyperparameter value:
    evaluate using validation set or cross-validation
Select best configuration
10. Key Insight
All ML models follow the same core loop:
    Prediction → Loss → Gradient → Update
Only these change:
    - model function
    - loss function
    - gradient expressions
