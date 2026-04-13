import numpy as np
X=np.random.randn(100)
#Y=2*X+1+noise
Y=2*X+1+np.random.randn(100)*0.1

#initialize parameters 
m,b=0,0
learning_rate=0.001
n=len(X)
epochs=100
for epoch in range(epochs):
      m_grad=0
      b_grad=0
      loss=0
      for i in range(n):
        x,y=X[i],Y[i]
        # Prediction
        y_pred=m*x+b
        #Error computattion
        error=y-y_pred
        #compute loss
        loss+=error**2
        #compute gradients
        m_grad+=-2*x*error
        b_grad+=-2*b
    #compute Average
    loss/=n
    m_grad/=n
    b_grad/=n
    #Update (Gradient DEscent)
    m=m-leraning_rate*m_grad
    b=b-leraning_rate*b_grad
  if epoch%100==0:
        print(f"Epoch {epoch}:Loss={loss:.4f}")
print("Final m:",m)
print("Final b:",b)
      
