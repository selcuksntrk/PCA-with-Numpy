# Numpy ile PCA (Temel Bileşen Analizi) işlemi


### PCA nedir?


PCA aslında bir boyut düşürme yöntemidir. Bilgiyi mümkün olduğunca koruyarak elimizdeki verinin boyutunu düşürür.
Bunu verinin içindeki değerlerin varyansına bakarak yapar. En çok varyansı içeren değerleri saklayarak orijinal veriden daha düşük boyutta fakat
orijinal verinin içerdiği bilgiyi belli bir oranda koruyarak izdüşümünü alır. Bu işlem aynı zamanda hesaplama maliyetini de düşürür, çünkü normalden daha düşük
boyutta bir veri elde etmiş oluruz. O veriyle hesaplamalar yapmak daha az işlem gücü gerektirir.


### PCA yaparken hangi adımlar uygulanır


- Veriyi merkeze alma işlemi

	Verinin ortalaması kendinden çıkarılarak gerçekleştirilir.

- Kovaryans matrisin hesaplanması

	Ayrıntılı bilgi için, [Kovaryans matrisi - Wikipedi](https://tr.wikipedia.org/wiki/Kovaryans_matrisi)

- Eigen vektörlerin ve eigen değerlerin hesaplanması

	Ayrıntılı bilgi için, [Özdeğer ayrışımı - Wikipedi](https://tr.wikipedia.org/wiki/%C3%96zde%C4%9Fer_ayr%C4%B1%C5%9F%C4%B1m%C4%B1)


- Her eigen değerin ne kadar varyansı içerdiğini hesaplıyoruz (yüzde üzerinden). Daha sonra varyansların kümülatif toplamını hesaplıyoruz. 
Böylece en çok varyansı kapsayan değerlerin varyansları toplamını görebiliriz. Belirlediğimiz varyans toplamını (genelde %95) sağlayan komponent sayısını düşürmek 
istediğimiz boyut (n) olarak belirliyoruz.


- Sonra, X matrisimizin ve özvektör matrisimizin iç çarpımını gerçekleştiririz, ancak yalnızca özvektör matrisinin ilk n sütununu alırız. 
Bu durumda n, orijinal verilerimizi azaltmak istediğimiz boyuttur. İç çarpım nedeniyle sonuç matrisi n sütuna sahip olacaktır. 
Böylece orijinal bilginin yüzde 95'ine sahip olan fakat daha düşük boyuta sahip bir matris elde ederiz. 

	Ayrıntılı bilgi için, [Nokta çarpım - Wikipedi](https://tr.wikipedia.org/wiki/Nokta_%C3%A7arp%C4%B1m)
