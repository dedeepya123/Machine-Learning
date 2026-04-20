# Overfitting

## 1. Where we are coming from

We started with a simple idea:
- Given data, learn a function that maps inputs to outputs
We modeled this using:
* Linear Regression → for continuous output
* Logistic Regression → for classification
In both cases:
Model:
f(x) = w·x + b
Goal:
Find weights (w) that minimize error on data
## 2. What we improved
We realized:
Real-world data is not always linear
So we:
* added features (x², x1*x2, etc.)
* transformed data
This made the model more powerful.
## 3. Hidden assumption
While training, we assume:
Training data represents the true pattern of the real world
## 4. Reality of data
In practice:
data = true pattern + noise
* pattern → what we want to learn
* noise → random, not useful
## 5. What should ideally happen
Model should learn:underlying pattern and ignore noise
## 6. What actually happens during training
We optimize:
Loss = error over all datapoints
Using gradient descent:
w = w - lr * gradient
### Learning behavior
* Initially → model learns general pattern
* Most datapoints get fit well
## 7. The critical stage
After some time:
* Most points → low error
* Few points → still have error (often noisy)
## 8. What model tries to do
To reduce loss further: Model tries to fit these remaining points
## 9. Important insight
Model is not trying to keep all good points intact. It only tries to reduce overall loss
## 10. What happens during updates
* Some bad points improve 
* Some already good points may worsen 
But if total loss decreases → update is accepted
## 11. Why weights become large
To fit those difficult/noisy points:
* small adjustments are not enough
* model needs bigger changes in output
### How does model create bigger changes?
By increasing weights
## 12. Meaning of large weights
Large weights make model: highly sensitive to inputs
### Example
* small weights → smooth changes
* large weights → sharp changes
## 13. What are “sharp changes”?
 Small change in input → large change in output
This creates a **wiggly / unstable function**
## 14. Final outcome
Model starts learning: very specific patterns that exist only in training data (noise)
## 15. Overfitting
Overfitting happens when the model learns noise by becoming too sensitive,leading to poor performance on new data.
## 16. Key Signals
* Training error → very low
* Test error → high
## 17. Final
* Early training → learning pattern
* Later training → chasing noise
* Result → unstable model
## 18. One-line takeaway
Overfitting is when a model becomes too flexible and uses large weights to fit noise instead of learning the true pattern.
