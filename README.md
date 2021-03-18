# PCA with Numpy

## TURKISH


Numpy ile PCA (Temel Bileşen Analizi) işlemi

Türkçe açıklamalar ve kod için TURKISH kalsörüne bakınız.


## ENGLISH

PCA with Numpy



### What is PCA


Pca is a process of dimension reduction. We can reduce the dimension with saving most of information.
Alse PCA helps us reduce the cost of computing, because of we deal with a matrix with lower dimension.



### How PCA is done?


- Centering the data

<img src="https://latex.codecogs.com/png.latex?\bg_white&space;\fn_cm&space;X^2" title="X^2" />


- Calculating covariance matrix of X

![equation](http://www.sciweavers.org/tex2img.php?eq=X%20%3D%20%28X%20-%20%20%5Cbar%7BX%7D%20%29&bc=White&fc=Black&im=png&fs=12&ff=arev&edit=0)

					![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cbar%7BX%7D&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0) is the mean of the n scores
					

	![equation](http://www.sciweavers.org/tex2img.php?eq=Cov%28X%29%20%3D%20%20%5Cfrac%7B1%7D%7Bn%20-%201%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20%28X_%7Bi%7D%20-%20%20%5Cbar%7BX%7D%20%29%20%28X_%7Bi%7D%20-%20%20%5Cbar%7BX%7D%20%29%5E%7BT%7D&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0)

	-n is the number of scores in each set of data
	-![equation](http://www.sciweavers.org/tex2img.php?eq=%5Cbar%7BX%7D&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0) is the mean of the n scores
	-![equation](http://www.sciweavers.org/tex2img.php?eq=X_%7Bi%7D%20&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0) is the raw score in the first set of scores

	Further information [Covariance matrix - Wikipedia](https://en.wikipedia.org/wiki/Covariance_matrix)

- Calculating eigenvectors and eigenvalues

    If we have a matrix X

    ![equation](http://www.sciweavers.org/tex2img.php?eq=Xv%20%3D%20%20%5Clambda%20v&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0)

    Rearranging this equation

    ![equation](http://www.sciweavers.org/tex2img.php?eq=%28X%20-%20%20%5Clambda%20I%29v%20%3D%200&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0)

    Solution exist only when the

    ![equation](http://www.sciweavers.org/tex2img.php?eq=%28X%20-%20%20%5Clambda%20I%29&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0)

    is singular. So this expression should be valid

    ![equation](http://www.sciweavers.org/tex2img.php?eq=det%28X%20-%20%20%5Clambda%20I%29%20%3D%200&bc=Transparent&fc=Black&im=png&fs=12&ff=iwona&edit=0)

    When we solve the characteristic polynomial, the roots of this polynomial will be the eigenvalues that we want.

    After we find the eigenvalues we can calculate the eigenvectors "v" by solving the equation above.


-Then we perform the dot product of our X matrix and the eigenvector matrix but only getting eigenvector matrix's first n columns. in this case the n is the dimension we want to reduce our original data. Because of the dot product the result will have n columns. So the data will be reduced successfully.
