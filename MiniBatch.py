def train_mini_batch(X_train, Y_train, lr=0.01, lam=0.01, batch_size=32):
      n_samples,n_features= X_train.shape
      W = np.zeros((num_features,1))
      bias = 0.0

      for epoch in range(epochs):
          indices = np.random.permutation[n_samples]
          X_train = X_train[indices]
          Y_train = Y_tarin[indices]

          for start in range(0,num_samples,batch_size):
              end = start + batch_size
              X_batch = X_train[start:end]
              Y_batch = Y_tarin[start:end]

              y_pred = X_batch@W + bias
              B = X_batch.shape[0]
              w_grad = (2/B) * (X_batch.T @ error) + 2*lam*W
              b_grad = (2/B) * np.sum(error)
              W -= lr * W_grad
              bias -= lr * b_grad
      return W,bias
