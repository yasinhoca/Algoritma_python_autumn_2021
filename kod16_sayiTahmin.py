#sayı tahmin oyunu
#bilgisayar sayı tutuyor
import random

sayi = random.randint(0,100)
sayac = 0
tahmin = int(input("Bir sayı tahmin ediniz :"))

while tahmin != sayi :
    sayac+=1
    if(sayac==10): #10 kere hak verdik, bilemezse döngüyü kırdık
        print("Hakkınız bitti!")
        break
    if sayi>tahmin:
        print("YUKARI")
        tahmin = int(input("Bir sayı tahmin ediniz :"))
    else:
        print("AŞAĞI")
        tahmin = int(input("Bir sayı tahmin ediniz :"))

if sayac<10: #sayac 10 a gelince tekrar yazmasın
    print("Tebrikler",sayac,"denemede bildiniz")