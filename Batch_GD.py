def train_batch(X_train,Y_train,epochs=10000,learning_rate=0.01,lam=0.01):
  n_samples,n_featues=X_train.shape
  
  W=np.zeros((num_features,1))
  bias=0.0
  
  for epoch in range(epochs):
    #forwrdPass
    y_pred = X_train @ W + bias
    #loss
    error = y_pred-Y_train
    data_loss = np.mean(error**2)
    reg_loss = lam*np.sum(W**2)
    loss = data_loss + reg_loss

    #compute Gradients
    w_grad = (2/n_samples)*(X_train.T*error) + 2*lam*W
    b_grad = (2/n_samples)*np.sum(error)

    W = W - learning_rate * w_grad
    bias = bias - learning_rate * b_grad
  return W,bias
    
    
      
