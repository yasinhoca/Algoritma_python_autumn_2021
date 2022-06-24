#0-50 arasında 10 sayı alacağız. Bunu diziye aktaracağız
#toplamları ve ortalamalarını bulacağız

dizi = []

for i in range(10):
    sayi = int(input("Bir sayı giriniz:"))
    while True:
        if(sayi>0 and sayi<50):
            dizi.append(sayi)
            break;
        else:
            print("Sıfır ile elli arasında sayı giriniz!")
            sayi = int(input("Bir sayı giriniz:"))

print(dizi)

toplam = 0
for i in range(len(dizi)):
    toplam += dizi[i]

#for i in dizi:  dizi elemanlarını tek tek alarak yapılan döngü
#    toplam +=i

print("toplam:",toplam)
print("ortalama:",toplam/len(dizi))



