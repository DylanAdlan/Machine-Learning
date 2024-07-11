'''
iexplore

1.
The maximal margin hyperplane is the separating hyperplane for which the margin is ______
- largest

2.
If _____ it lies on one side positive half space of the hyperplane
- W^T X > C

3.
SVM is used for _____
- Classification and Regression

4.
property of an SVM
- Overfitting can be controlled by soft margin approach

5.
When the tuning parameter C is _____, then the margin is wide, many observations violate the margin, and so there are many support vectors.
- Large

6.
The hyperplane that separates the two sets of data is called the _______.
- Linear Discriminant

7.
If _____ it lies on other side negative half space of the hyperplane
- W^T X < C

8.
The _______ distance is called the minimal distance between the hyperplane and the observation, and it is called margin.
- shortest

9.
For every linearly separable data, there exist _______ number of separating hyperplanes
- infinite

10.
The effectiveness of an SVM depends upon
- Selection of Kernel
- Kernel Parameters
- Soft Margin Parameter C

ianalyse

1.
Suppose you are building a SVM model on data X. The data X can be error prone which means that you should not trust any specific data point too much. Now think that you want to build a SVM model which has quadratic kernel function of polynomial degree 2 that uses Slack variable C as one of it’s hyper parameter. Based upon that give the answer for following question.

What would happen when you use very large value of C(C->infinity)?
Note: For small C was also classifying all data points correctly
- We can still classify data correctly for given setting of hyper parameter C

2.
The SVM’s are less effective when
- The data is noisy and contains overlapping points

3.
The cost parameter in the SVM means:
- The tradeoff between misclassification and simplicity of the model

4.
Support vectors are the data points that lie closest to the decision surface.
- True

5.
real world applications of the SVM
- Text and Hypertext Categorization
- Image Classification
- Clustering of News Articles

6.
Suppose you are using RBF kernel in SVM with high Gamma value. What does this signify?
- The model would consider only the points close to the hyperplane for modeling

7.
true about kernel in SVM?
- Kernel function map low dimensional data to high dimensional space
- Its a similarity function

8.
If I am using all features of my dataset and I achieve 100% accuracy on my training set, but ~70% on validation set, what should I look out for?
- Overfitting

9.
When the C parameter is set to infinite, which of the following holds true?
- The optimal hyperplane if exists, will be the one that completely separates the data

10.
What do you mean by generalization error in terms of the SVM?
- How accurately the SVM can predict outcomes for unseen data









'''