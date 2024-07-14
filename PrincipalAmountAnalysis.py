'''
PCA - teknik utk reduce dimensionality while preserve variability as much as possible in dataset

iexplore

1.
Principal component in PCA represent
- A linear combination of original features

2.
Primary goal of Principal Component Analysis (PCA)
- Dimensionality reduction

3.
Principal components ordered in PCA
- By their eigenvalues in descending order

4.
In PCA, explained variance ratio indicate
- The amount of variance captured by each principal component

5.
PCA handle multicollinearity among features
- By combining correlated features into principal components

6.
In PCA, maximum number of principal components that can be obtained is
- Equal to the number of non-zero eigenvalues

7.
Primary application of PCA in machine learning is
- Dimensionality reduction

8.
- PCA is an unsupervised learning technique (True)
- PCA is a classification algorithm (False)
- PCA is a clustering algorithm (False)
- PCA is a supervised learning technique (False)

9.
Purpose of the scree plot in PCA is
- To visualize the cumulative variance explained by each principal component

10. 
Steps of PCA
- Standardize the data
- covariance matrix computation
- eigenvalue and eigenvector calculation
- principal components selection
- transform data

ianalyse

1.
Relationship between eigenvalues and principal components in PCA
- Eigenvalues indicate the amount of variance explained by each principal component

2.
PCA handle missing values in the dataset
- By imputing the missing values

3.
Primary goal of PCA in exploratory data analysis
- To reduce the dimensionality of the data

4.
NOT a common application of PCA - Text mining
Common - Image compression, Market segmentation, gene expression analysis

5 & 6
True abt PCA 
- is sensitive to the scale of the variables and 
- is sensitive to outliers bcs it relies on the variance in the data
- not increase the interpretability of the data so can lead to loss of interpretability
- not preserve all features
- applicable to high-dimensional data

False 
- PCA requires categorical variables
- PCA assumes that the data is normally distributed
- PCA can only handle linear relationships between variables

7.
PCA help in data visualization
- by decrese the dimensionality of data for plotting

8.
Primary disadvantage of PCA
- can lead to loss of interpretability

9.
In PCA, role of the loading scores is 
- They represent the weights of each original feature in the principal components

10.
Primary difference between PCA and factor analysis
- PCA assumes linear relationships between variables, while factor analysis does not

'''