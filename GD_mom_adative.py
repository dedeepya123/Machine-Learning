def train_batch(X_train, Y_train, epochs=10000, lr=0.01, lam=0.01, beta=0.9, beta_2=0.999, eps=e-8 ):
      n_samples, n_features = X_train.shape

      W = np.zeros((n_features , 1))
      bias = 0.0
      # first moment (momemtum)
      m_w = np.zeros_like(W)
      m_b = 0.0

      #second moment (adaptive Scaling)
      v_w = np.zeros_like(W)
      v_b = 0.0
  
      for t in range(epochs):
            y_pred = X @ W + bias
            
            #compute losss
            error = y_pred - Y
            data_loss = np.mean(error**2) 
            reg_loss = lam * np.sum(W**2)
            loss = data_loss + reg_loss
            
            #compute grad
            w_grad = (2/n_samples)*(X.T @ error) + 2 * lam * W
            b_grad = (2/n_samples) * error

            # momentum update 
            m_t = beta1 * m_w + (1 - beta1) * w_grad
            m_b = beta1 * m_b + (1 - beta1) * b_grad

            #second moment update
            v_w = beta2 * v_w + (1 - beta2) * (w_grad**2)
            v_b = beat2 * v_b + (1 - beta2) * (b_grad**2)

            # bias correction
            m_w_hat = m_w / (1 - beta1**t)
            m_b_hat = m_b / (1 - beta1**t)
            
            v_w_hat = v_w / (1 - beta2**t)
            v_b_hat = v_b / (1 - beat2**t)

            W -= lr * (m_w_hat / (np.sqrt(v_w_hat) + eps))
            bias -= lr * (b_w_hat / (np.sqrt(v_b_hat) +eps))

    return W,bias
            
