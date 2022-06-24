#class-sınıf ve object-nesne kavramı

ad = "ali"    #global
soyad = "öz"

class ogrenci:
    #global ad, soyad   #global değişken kullanılacaksa yazılır
    ad = "Mehmet" #local
    soyad = "Can"
    #v = 50
    #f = 80

    def yazdir(self):
        print(self.ad)
        print(self.soyad)
        #print(ad,soyad)

    def ortalama(self,v,f):
        #return self.v*0.4+self.f*0.6 #localdeki v ve f değişkenleri için
        return v*0.4+f*0.6




nesne = ogrenci()
#print(nesne.ad)
#print(nesne.soyad)
#nesne.ad = "Yasin"
#nesne.soyad = "Sağlam"
#print(nesne.ad)
#print(nesne.soyad)
nesne.yazdir()
print(nesne.ortalama())







