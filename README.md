# PCA with Numpy

## TURKISH


Numpy ile PCA (Temel Bileşen Analizi) işlemi

Türkçe açıklamalar ve kod için TURKISH kalsörüne bakınız.


## ENGLISH

PCA (Principal Component Analysis) with Numpy


### What is PCA


PCA is actually a dimension reduction method. It reduces the dimension of the data we have by protecting the information as much as possible. 
It does this by looking at the variance of the values in the data. It takes the projection by storing the values that contain the most variance. 
At the end, the pca applied data has lower dimension than the original data, but preserving the information contained in the original data to a certain extent. 
This process also reduces the computational cost because we get a lower-than-normal size of data. It takes less processing power to make calculations with that data.


### How PCA is done


- Centering the data

	By substracting the mean of our data from itself.


- Calculating covariance matrix of X

	Further information [Covariance matrix - Wikipedia](https://en.wikipedia.org/wiki/Covariance_matrix)


- Calculating eigenvectors and eigenvalues

	Further information [Eigenvalues and eigenvectors - Wikipedia](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)


- We calculate how much variance each eigen value contains (in percentage). We then calculate the cumulative sum of variances. 
Thus, we can see the sum of the variances of the values that include the most variance. We determine the number of components that provide the total 
variance we want to cover (generally 95%) as the dimension (n) we want to reduce.


- Finally, we perform the dot product of our X matrix and our eigenvector matrix, but we only take the first n columns of the eigenvector matrix. 
In this case, n is the size we want to reduce our original data to. Due to the inner product, the resulting matrix will have n columns. 
So we get a matrix that has 95 percent of the original information but has a lower dimension.

	Further information [Dot product - Wikipedia](https://en.wikipedia.org/wiki/Dot_product)
