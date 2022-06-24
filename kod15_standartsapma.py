# 10000 sayı ile standart sapma
import random
import math

dizi = []
toplam = 0

for i in range(10000):
    dizi.append(random.randint(0,100))
    toplam += dizi[i]

#print(dizi)
print("Toplam=",toplam)
ort = toplam/len(dizi)
print("Ortalama=",ort)

varyans = []

for i in range(len(dizi)):
    v = math.pow((dizi[i]-ort),2)
    varyans.append(v)

#print(varyans)

vtoplam = 0

for i in range(len(varyans)):
    vtoplam += varyans[i]

print(vtoplam)

sp = math.sqrt(vtoplam/(len(varyans)-1))

print("Standart sapma =",sp)
