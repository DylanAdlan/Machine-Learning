'''
iexplore

1.
K-Means clustering is a single-shot process (False)

2.
Considering the K-means algorithm, if points (5,3), (2,8), and (-1, 4) are the only points which are assigned to the first cluster now, 
what is the new centroid for this cluster?
- (2,5)

3.
By Increasing the Clustering values,variance in the data point is also increase (False)

4.
Considering the K-means algorithm, derived the 3 centroids (O, 1) (2, 1), (-1, 2)
can the following point (2, 3) and (2, O.5) be assigned to the same cluster in the next iteration?
- √8

5.
Typically , clustering algorithm decides how many clusters to make on its own looking at the data (False)

6.
The number of seeds thrown on a given dataset will be 2 when we want algorithm to give back 4 clusters (False)

7.
Use K-Means Algorithm to create two clusters( C1 & C2),Assume A(2, 2) and C(1, 1) are the initial centers of the two clusters
For the First iteration,the following points are grouped in which cluster
- A(2,2) belongs to => C1
- B(3,2) belongs to => C1
- C(1,1) belongs to => C2
- D(3,1) belongs to => C1
- E(1.5,0.5) belongs to => C2

8.
Assume, you want to cluster 7 observations into 3 clusters using K-Means clustering algorithm. After first iteration clusters, C1, C2, C3 has following observations:

C1: {(5,3), (3,5), (7,1)}

C2: {(1,4), (4,2)}

C3: {(6,7), (8,9)}

What will be the cluster centroids if you want to proceed for second iteration?

a) Centroid for data points in cluster C1 (5,3)
b) Centroid for data points in cluster C2 (2.5,3)
c) Centroid for data points in cluster C3 (7,8)

9.
Suppose we want to group the visitors to the website using just their age (one-dimensional space) as follows
15,22,16,28,25,54,32
K= 2 initial centroid C1= 15 and C2 = 25,

a) After 1st iteration 22 belongs to which cluster (C2)
b) After 1st iteration 16 belongs to which cluster (C1)
c) After 1st iteration 54 belongs to which cluster (C2)
d) What is the new centroid value( C1,C2) after 1st iteration (15.5, 32.2)

10.
1) The number of seeds thrown on a given dataset has no relation to how many clusters we are looking for
(False)

ianalyse

1.
clustering type has characteristic shown in the below figure?
- Hierachical

2.
Hierarchical clustering should be primarily used for exploration.
- True

3.
Which of the following is valid iterative strategy for treating missing values before clustering analysis?
- Imputation with Expectation Maximization algorithm

4. (True abt K Means Clustering)
a) K-means is extremely sensitive to cluster center initializations
b) Bad initialization can lead to Poor convergence speed
c) Bad initialization can lead to bad overall clustering

5.
Movie Recommendation systems are an example of:
- Clustering
- Reinforcement Laerning

6.
Those metrics is used for finding dissimilarity between two clusters in hierarchical clustering?
- Single-link
- Complete-link
- Average-link

7.
Possible termination conditions in K-Means

- For a fixed number of iterations.
- Assignment of observations to clusters does not change between iterations. Except for cases with a bad local minimum.
- Centroids do not change between successive iterations.
- Terminate when RSS falls below a threshold.

8.
Feature scaling is an important step before applying K-Mean algorithm. What is reason behind this?
- In distance calculation it will give the same weights for all features

9.
Cases when K-Means clustering fail to give good results?
- Data points with outliers
- Data points with different densities
- Data points with non-convex shapes

10.
False
- K-nearest neighbor is same as k-means
True
- K-means clustering is a method of vector quantization
- K-means clustering aims to partition n observations into k clusters








'''