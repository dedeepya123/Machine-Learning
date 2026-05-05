def SGD(X_train,Y_train, epochs=10000, lr=0.01, lam=0.01):
    n_samples, n_features = X_train.shape

    W = np.zeros((num_features,1))
    bias = 0.0

    for epoch in range(epochs):
        for i in range(num_samples):
            x_i = X_train[i].reshape(1,-1)
            y_i = Y_train[i]

            y_pred = x_i@W + bias

            error = y_pred - y_i
            w_grad = 2*x_i.T @ error + 2*lam*W
            b_grad = 2*error
            W-=lr * w_grad
            bias-= lr * b_grad
  return W,bias
            
