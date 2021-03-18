# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:50:20 2020

@author: Selcuk Senturk, selcuksntrk@gmail.com
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



#Görselleştirme için bazı ayarlar

plt.style.use("ggplot")

plt.rcParams["figure.figsize"] = (12,8)





#----------Veriyi içeri aktarma----------#



data = pd.read_csv('data.csv', header=None)




#Centering işlemi (centering işleminin Türkçe karşılığından tam emin değilim,
#veriyi merkezi hale getirme diyebiliriz)

data = data - np.mean(data, axis=0)





#----------Eigen vektörleri ve eigen değerleri bulma----------#




#Önce kovaryans matrisi buluyoruz
#bunu yapmak için np.cov fonksiyonunu kullanıyoruz

covariance_matrix = np.cov(data, rowvar = False)





#daha sonra np.linalg.eigh fonksiyonu ile eigen vektörleri
#ve eigen değerleri buluyoruz

eigen_values, eigen_vectors = np.linalg.eigh(covariance_matrix)





#Eigen vektörleri ve eigen değerleri büyükten küçüğe doğru sıralıyoruz
#bu bize hangi değerleri seçeceğimiz hesaplamada büyük kolaylık sağlıyor

indexes = eigen_values.argsort()[::-1]

eigen_values = eigen_values[indexes]

eigen_vectors = eigen_vectors[:,indexes]





#----------Açıklanmış varyans ile temel bileşenleri seçiyoruz----------#



#Her eigen değerin ne kadar varyansı içerdiğini hesaplıyoruz (yüzde üzerinden)

variance_explained = [(i/sum(eigen_values))*100 for i in eigen_values]





#Varyansların kümülatif toplamını hesaplıyoruz. Böylece en çok varyansı kapsayan
#değerlerin varyansları toplamını görebiliriz.


cumulative_variance_explained = np.cumsum(variance_explained)



#Kümülatif toplamın grafiğini çizdiriyoruz
#Böylece veriyi daha iyi analiz edebiliriz.
#X ekseni burada komponent sayısını temsil ediyor


xs = [(i) for i in range(data.shape[1])]

plt.plot(xs, cumulative_variance_explained)

plt.xlabel("Komponent Sayısı")

plt.ylabel("Kümülatif Varyans")

plt.title("Kümülatif Varyans vs Komponent Sayısı")

plt.show()








#Son olarak elimizdeki matrisin boyutunu düşürme aşamasına geçebiliriz.
#Bu işlemi orijinal veri matrisimiz ile eigenvektörün iç çarpımını hesaplayarak yapacağız.



#Ama önce veri matrisimizi hangi boyuta düşüreceğimizi belirlememiz gerekiyor.
#Bunu varyansı belli bir değerde belirleyerek yapabiliriz.
#Mesela bu örnekte toplam varyansın yüzde 95'ini kapsayan komponent sayısını tespit edip
#veri matrisimizi o boyuta indirgiyoruz. (Genelde yüzde 95 varyans kullanılır).

variance = 95

n_component = 0

for i in range(0, len(cumulative_variance_explained)):
    
    if cumulative_variance_explained[i] <= variance:

        continue
    else:

        n_component = i - 1

        break




#Komponent sayısını belirledikten sonra (n_component)
#eigen vektörümüzün ilk n_component komponentini seçiyoruz
#(daha önce büyükten küçüğe sıraladığımız için bu şekilde yapabiliyoruz.)

eigen_vectors = eigen_vectors[:, :n_component]




#Boyut düşürme işlemini gerçekleştiriyoruz

data_pca_applied = np.dot(data, eigen_vectors)






#----------PCA uygulanmış veriyi incelemek için bir kaç çizim yaptırabiliriz----------#


plt.plot(data_pca_applied[:,0], data_pca_applied[:,1], "ro")
plt.title("PCA Komponent 1 vs PCA Komponent 2")
plt.show()



plt.plot(data_pca_applied[:,0], data_pca_applied[:,2], "ro")
plt.title("PCA Komponent 1 vs PCA Komponent 3")
plt.show()



plt.plot(data_pca_applied[:,0], data_pca_applied[:,3], "ro")
plt.title("PCA Komponent 1 vs PCA Komponent 4")
plt.show()



plt.plot(data_pca_applied[:,0], data_pca_applied[:,4], "ro")
plt.title("PCA Komponent 1 vs PCA Komponent 5")
plt.show()







#PCA uygulanmış veriyi diske kaydetme işlemi

np.savetxt("data_pca_applied.csv", data_pca_applied, delimiter=",")




