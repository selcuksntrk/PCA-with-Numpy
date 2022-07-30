# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:50:20 2020

@author: Selcuk Senturk, selcuksntrk@gmail.com

Bu kod PCA işlemini Scikitlearn'in PCA fonksiyonu ile aynı şekilde yapar
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys


plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (12,8)                 #Görselleştirme için ayarlamalar


def centeringData(data, axis=0):                        #Verilere merkezleme işlemi uygulama
    centeredData = data - np.mean(data, axis=axis)
    return centeredData


def calculateCovarianceMatrix(data):                    #Kovaryans matrisini hesaplama
    covarianceMatrix = np.cov(data, rowvar = False)     #Bunu yapmak için np.cov fonksiyonunu kullanıyoruz
    return covarianceMatrix


def calculateEigens(covarianceMatrix):                  #Özdeğerleri ve özvektörleri bulma
    eigenValues, eigenVectors = np.linalg.eigh(covarianceMatrix)
    return eigenValues, eigenVectors


def sortEigens(eigenValues, eigenVectors, order=-1):    #order = -1 ise azalan, 1 ise artan.
    indexes = eigenValues.argsort()[::-1]               #özdeğerler ve özvektörler büyükten küçüğe sıralandı
    sortedEigenValues = eigenValues[indexes]
    sortedEigenVectors = eigenVectors[:,indexes]
    return sortedEigenValues, sortedEigenVectors


#Explained Variance Yöntemi ile ana bileşenleri seçeceğiz
def findVarianceExplained(eigenValues):                 #Her bir öz değerin ne kadar varyansı olduğunu bulma (yüzde olarak)
    varianceExplained = [(i/sum(eigenValues))*100 for i in eigenValues]
    return varianceExplained


def findCumulativeVarExp(varianceExplained):             #Özdeğerlerin varyanslarının kümülatif toplamını bulma
    cumulativeVarianceExplained = np.cumsum(varianceExplained)  #Bu değer, her bir öz değeri dahil ettiğimizde ne kadar varyansa sahip olacağımızı gösterir.
    return cumulativeVarianceExplained


def plotCumulativeVarExp(cumulativeVarianceExplained, data, x_label="Number of Component", y_label="Cumulative variance", title="Cumulative variance vs Number of Component"):
    xs = [(i) for i in range(data.shape[1])]
    plt.plot(xs, cumulativeVarianceExplained)           #Bu kümülatif toplamı grafiksel olarak çizme
    plt.xlabel(x_label)                                 #Burada x ekseni, bileşenlerin sayısını belirtir
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


def findN(cumulativeVarianceExplained, variance=95):      
    variance = variance
    nComponent = 0
    
    for i in range(0, len(cumulativeVarianceExplained)):    #Azaltılacak bileşenlerin sayısını belirleme süreci.
        if cumulativeVarianceExplained[i] <= (variance):    #Bunu, kapsamasını istediğimiz varyans miktarını tanımlayarak yapabiliriz.
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
    eigenVectors = eigenVectors[:, :n]  #Özvektörlerin ilk n bileşenini seçiyoruz
    dataPcaApplied = np.dot(data, eigenVectors) #Boyut küçültme gerçekleştirme
    return dataPcaApplied
    

def plotPcaComponents(dataPcaApplied, compOne=0, compTwo=1): #PCA bileşenlerini çizdirme
    plt.plot(dataPcaApplied[:,compOne], dataPcaApplied[:,compTwo], "ro")
    title = "PCA Component " + str(compOne+1) +" vs PCA Component " + str(compTwo+1)
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
    
    #En iyi varyans değerini bulmak için kümülatif varyans grafiği çizebiliriz
    findBestVariance(data) #Bu veriler için en iyi varyans değeri, grafik türevinin önemli ölçüde düşük olduğu, yani varyansın yüzde 95 civarında olduğu yerdir.
    dataPcaApplied = PCA(data, variance=95)
    
    #Verileri incelemek için uygulanan veri pca'nın bazı bileşenlerini çizebiliriz.
    plotPcaComponents(dataPcaApplied, compOne=0, compTwo=1) #komponent 1 vs 2
    plotPcaComponents(dataPcaApplied, compOne=1, compTwo=2) #komponent 2 vs 3
    plotPcaComponents(dataPcaApplied, compOne=0, compTwo=2) #komponent 1 vs 3
    
    #PCA uygulanan verileri dışa aktarma
    file_name = "dataPcaApplied.csv"
    exportData(dataPcaApplied, file_name=file_name)