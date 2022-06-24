toplam = 0
sayac = 0
#toplam = sayac = 0 bu yapıda kullanılabilir

for i in range(50,600):
    if i%3==0:
        toplam+=i
        sayac+=1

ort = toplam / sayac

print("Toplam =",toplam)
print("3'e bölünen sayı adedi =",sayac)
print("Ortalama = ",ort)