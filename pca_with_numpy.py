# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:50:20 2020

@author: Selcuk Senturk, selcuksntrk@gmail.com
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#Adjustments for visualization

plt.style.use("ggplot")

plt.rcParams["figure.figsize"] = (12,8)





#----------Importing the data----------#



data = pd.read_csv('data.csv', header=None)




#Applying centering to data

data = data - np.mean(data, axis=0)





#----------Finding Eigenvalues and Eigenvectors----------#




#First we need to find the covariance matrix
#To do this, we use np.cov function

covariance_matrix = np.cov(data, rowvar = False)





#Then we find the eigenvalues and eigenvectors

eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)





#we sort the eigenvalues and eigenvectors in descending order

indexes = eigen_values.argsort()[::-1]

eigen_values = eigen_values[indexes]

eigen_vectors = eigen_vectors[:,indexes]





#----------We choose the principal components with Explained Variance Method----------#



#Finding out how much variance each eigen value has (in percentage)

variance_explained = [(i/sum(eigen_values))*100 for i in eigen_values]





#The process of finding the cumulative sum of variances of eigen values.
#This value shows how much variance we will have when we include each eigen value.


cumulative_variance_explained = np.cumsum(variance_explained)



#Plotting this cumulative sum graphically
#x-axis here denotes the number of components


xs = [(i) for i in range(data.shape[1])]

plt.plot(xs, cumulative_variance_explained)

plt.xlabel("Number of Component")

plt.ylabel("Cumulative variance")

plt.title("Cumulative variance vs Number of Component")

plt.show()








#Finally, we move on to reducing the size of the data matrix.
#This process is carried out by taking the dot product of our data matrix and eigenvector matrix



#The process of determining the number of components to be reduced.
#We can do this by determining the amount of variance we want it to cover.

variance = 95

n_component = 0

for i in range(0, len(cumulative_variance_explained)):
    
    if cumulative_variance_explained[i] <= variance:

        continue
    else:

        n_component = i - 1

        break




#We choose the first n_component of eigenvectors (we ordered them before)

eigen_vectors = eigen_vectors[:, :n_component]




#Performing dimension reduction.

data_pca_applied = np.dot(data, eigen_vectors)






#----------We can plot some of the component to analyze PCA applied data----------#


plt.plot(data_pca_applied[:,0], data_pca_applied[:,1], "ro")
plt.title("PCA Component 1 vs PCA Component 2")
plt.show()



plt.plot(data_pca_applied[:,0], data_pca_applied[:,2], "ro")
plt.title("PCA Component 1 vs PCA Component 3")
plt.show()



plt.plot(data_pca_applied[:,0], data_pca_applied[:,3], "ro")
plt.title("PCA Component 1 vs PCA Component 4")
plt.show()



plt.plot(data_pca_applied[:,0], data_pca_applied[:,4], "ro")
plt.title("PCA Component 1 vs PCA Component 5")
plt.show()







#Saving the numpy array that contains PCA applied data values

np.savetxt("data_pca_applied.csv", data_pca_applied, delimiter=",")




