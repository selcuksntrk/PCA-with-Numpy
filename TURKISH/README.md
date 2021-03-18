# PCA with Numpy

## TURKISH


Numpy ile PCA (Temel Bileşen Analizi) işlemi

Türkçe açıklamalar ve kod için TURKISH kalsörüne bakınız.


## ENGLISH

PCA (Principal Component Analysis) with Numpy


### What is PCA


Pca is a process of dimension reduction. We can reduce the dimension with saving most of information.
Alse PCA helps us reduce the cost of computing, because of we deal with a matrix with lower dimension.


### How PCA is done


- Centering the data

	By substracting the mean of our data from itself.

- Calculating covariance matrix of X

	Further information [Covariance matrix - Wikipedia](https://en.wikipedia.org/wiki/Covariance_matrix)

- Calculating eigenvectors and eigenvalues

	Further information [Eigenvalues and eigenvectors - Wikipedia](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)


-Then we perform the dot product of our X matrix and the eigenvector matrix but only getting eigenvector matrix's first n columns. 
In this case the n is the dimension we want to reduce our original data. Because of the dot product the result will have n columns. 
So the data will be reduced successfully.

	Further information [Dot product - Wikipedia](https://en.wikipedia.org/wiki/Dot_product)
