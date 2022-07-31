# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:50:20 2020

@author: Selcuk Senturk, selcuksntrk@gmail.com

This code does PCA exactly the same with ScikitLearn PCA function
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (12,8)                 #Adjustments for visualization


def centeringData(data, axis=0):                        #Applying centering to data
    centeredData = data - np.mean(data, axis=axis)
    return centeredData


def calculateCovarianceMatrix(data):                    #We need to find the covariance matrix
    covarianceMatrix = np.cov(data, rowvar = False)     #To do this, we use np.cov function
    return covarianceMatrix


def calculateEigens(covarianceMatrix):                  #We find the eigenvalues and eigenvectors
    eigenValues, eigenVectors = np.linalg.eigh(covarianceMatrix)
    return eigenValues, eigenVectors


def sortEigens(eigenValues, eigenVectors, order=-1):    #If order is -1 then descending, if 1 ascending.
    if order == -1:
        indexes = eigenValues.argsort()[::-1]               #we sort the eigenvalues and eigenvectors in descending order
    elif order == 1:
        indexes = eigenValues.argsort()[::]               #we sort the eigenvalues and eigenvectors in descending order
    sortedEigenValues = eigenValues[indexes]
    sortedEigenVectors = eigenVectors[:,indexes]
    return sortedEigenValues, sortedEigenVectors


#We will choose the principal components with Explained Variance Method
def findVarianceExplained(eigenValues):                 #Finding out how much variance each eigen value has (in percentage)
    varianceExplained = [(i/sum(eigenValues))*100 for i in eigenValues]
    return varianceExplained


def findCumulativeVarExp(varianceExplained):             #The process of finding the cumulative sum of variances of eigen values.
    cumulativeVarianceExplained = np.cumsum(varianceExplained)  #This value shows how much variance we will have when we include each eigen value.
    return cumulativeVarianceExplained


def plotCumulativeVarExp(cumulativeVarianceExplained, data, x_label="Number of Component", y_label="Cumulative variance", title="Cumulative variance vs Number of Component"):
    xs = [(i) for i in range(data.shape[1])]
    plt.plot(xs, cumulativeVarianceExplained)           #Plotting this cumulative sum graphically
    plt.xlabel(x_label)                                 #x-axis here denotes the number of components
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def findN(cumulativeVarianceExplained, variance=95): 
    variance = variance
    nComponent = 0
    
    for i in range(0, len(cumulativeVarianceExplained)):  #The process of determining the number of components to be reduced.
        if cumulativeVarianceExplained[i] <= (variance):    #We can do this by defining the amount of variance we want it to cover.
            continue
        else:
            nComponent = i - 1
            break
    return nComponent


def findBestVariance(data):
    data = centeringData(data, axis=0)
    covarianceMatrix = calculateCovarianceMatrix(data)
    eigenValues, eigenVectors = calculateEigens(covarianceMatrix)
    eigenValues, eigenVectors = sortEigens(eigenValues, eigenVectors, order=-1)
    varianceExplained = findVarianceExplained(eigenValues)
    cumulativeVarianceExplained = findCumulativeVarExp(varianceExplained)
    plotCumulativeVarExp(cumulativeVarianceExplained, data, x_label="Number of Component", y_label="Cumulative variance", title="Cumulative variance vs Number of Component")
    
    
def PCA(data, variance=95):
    data = centeringData(data, axis=0)
    covarianceMatrix = calculateCovarianceMatrix(data)
    eigenValues, eigenVectors = calculateEigens(covarianceMatrix)
    eigenValues, eigenVectors = sortEigens(eigenValues, eigenVectors, order=-1)
    varianceExplained = findVarianceExplained(eigenValues)
    cumulativeVarianceExplained = findCumulativeVarExp(varianceExplained)
    plotCumulativeVarExp(cumulativeVarianceExplained, data, x_label="Number of Component", y_label="Cumulative variance", title="Cumulative variance vs Number of Component")
    n = findN(cumulativeVarianceExplained, variance=variance)
    eigenVectors = eigenVectors[:, :n]  #We choose the first n_component of eigenvectors
    dataPcaApplied = np.dot(data, eigenVectors) #Performing dimension reduction.
    return dataPcaApplied
    

def plotPcaComponents(dataPcaApplied, compOne=1, compTwo=2): #Plot PCA component vs another component
    if (compOne < 1) or (compTwo < 1):
        print ("\n\ncompOne or compTwo cannot be lower than one, please try again with proper values!!!\n\n")
        sys.exit(1)
    elif (compOne > dataPcaApplied.shape[1]) or (compTwo > dataPcaApplied.shape[1]):
        print ("\n\ncompOne or compTwo cannot be higher than the column number of dataPcaApplied, please try again with proper values!!!\n")
        print("The column number of dataPcaApplied is:\t", dataPcaApplied.shape[1])
        print("\n\n")
        sys.exit(1)
    plt.plot(dataPcaApplied[:,compOne-1], dataPcaApplied[:,compTwo-1], "ro")
    title = "PCA Component " + str(compOne) +" vs PCA Component " + str(compTwo)
    plt.title(title)
    plt.show()


def exportData(dataPcaApplied, file_name="dataPcaApplied.csv"):
    np.savetxt(file_name, dataPcaApplied, delimiter=",")
    print("File created Successfully.")


if __name__ == '__main__':
    inputFileName = 'data.csv'
    
    try:
        data = pd.read_csv(inputFileName, header=None)
    except IOError:
        print ("[__main__]: ERROR Couldn't open input file " + inputFileName + ", exiting...\n")
        sys.exit(1)
    
    #To find the best variance value we can plot cumulative variance graph
    findBestVariance(data) #For this data, best variance value is where the graph derivative is dramatically low, which is around 95 percent
    dataPcaApplied = PCA(data, variance=95)
    
    #We can plot some components of the data pca applied to examine the data
    plotPcaComponents(dataPcaApplied, compOne=1, compTwo=2) #Component 1 vs 2
    plotPcaComponents(dataPcaApplied, compOne=2, compTwo=3) #Component 2 vs 3
    plotPcaComponents(dataPcaApplied, compOne=1, compTwo=3) #Component 1 vs 3
    
    #Exporting the PCA applied data
    file_name = "dataPcaApplied.csv"
    exportData(dataPcaApplied, file_name=file_name)