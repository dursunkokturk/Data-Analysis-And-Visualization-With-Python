# x Eksenindeki Degeri y Eksenindeki Karsiligini Alarak Grafik Goruntusunu Hesapliyoruz

import matplotlib.pyplot as matplot

x=[0,1,2,3]
y=[20,40,10,100]

fig, graphic= matplot.subplots()

# Verilen x ve y Ekseni Degerlerine Gore plot Komutu Ile Grafik Cizimini Yapiyoruz
graphic.plot(x, y)

# Cizilen Grafik Gosteriliyor
matplot.show()