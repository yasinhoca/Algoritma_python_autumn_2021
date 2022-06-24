# bir fonksiyon def öneki ile tanımlanır
#fonksiyonları programın üstüne yazmayı alışkanlık edinelim

def hosgeldin(): #parametre almayan fonksiyon
    print("Hoşgeldin")

hosgeldin() #fonksiyonu ana satırdan çağırıyoruz
hosgeldin()
hosgeldin()

def merhaba(isim): #fonksiyon parametre alıyor
    print("merhaba",isim)

isim = input("isminizi giriniz:")
merhaba(isim)

def carp(a,b):
    return a*b

print(carp(3,5))
