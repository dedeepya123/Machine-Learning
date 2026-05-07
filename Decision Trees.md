## Why do we need Decision Trees?
- We know models like Linear Regression and Logistic Regression. These models learn a global function: y = Wx + b or a linear decision boundary.
- This works well when the relation between features and target is approximately linear.

But in real-world data, relationships are often:
- non-linear
- conditional
- rule-based
- hierarchical
Example:

IF age > 30 AND income > 10L → Buy
ELSE IF student → Maybe Buy
ELSE → No Buy

Even after feature engineering, linear models may still struggle to learn such complex relationships naturally.
So we need a model that can learn non-linear decision boundaries directly from data.

## Core Idea of Decision Trees
- Decision Trees learn by making a sequence of rule-based decisions.
- Instead of learning one global function, a Decision Tree learns: hierarchical local decisions
At each step, the tree asks a question such as:
Age > 30 ? Based on the answer, data is split into smaller regions.
The process continues recursively.
Thus, Decision Trees perform:
- recursive partitioning of feature space

## How does a Decision Tree learn?

At every node, the tree tries to find: 
- the best feature to split
- the best threshold/value to split on such that the resulting child nodes become more pure
  
Example:
Age	Buy
20	No
22	No
45	Yes
50	Yes
A split like:
Age > 30
creates two cleaner groups.

## Challenges in Learning a Tree
While building the tree, several questions arise:
1. Which feature should we split on?
Many features may partially separate the data.
2. Where should we split?
Example:
Age > 20 ?
Age > 30 ?
Age > 40 ?
Which threshold creates the best separation?
3. When should we stop splitting?
If we keep splitting forever:
- tree memorizes training data
- leading to overfitting.
4. Among many possible trees, which one is better?
We need a way to evaluate split quality.

## Impurity
A node is impure if it contains mixed classes.
Example:
Samples	Label
50%	Yes
50%	No
This node has high uncertainty.
A pure node contains mostly one class.

## Goal of Decision Trees:
reduce impurity after every split

## Measures of Impurity
Two common impurity measures are:
### Entropy
Measures uncertainty/randomness in a node.
high entropy → mixed classes
low entropy → pure classes

### Gini Impurity
Measures how often a randomly chosen sample would be misclassified.
high gini → mixed classes
low gini → pure classes

### Information Gain

A split is good if it significantly reduces impurity.
This reduction is called:
Information Gain = Impurity(before split) - Impurity(after splait)

At every node, the Decision Tree chooses:
split with maximum information gain
