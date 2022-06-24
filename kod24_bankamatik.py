cp = int(input("Çekmek istediğiniz para:"))

while True:
    if(cp%10==0):
        break
    else:
        cp = int(input("Çekmek istediğiniz para 10 nun katları olsun lütfen:"))

if cp>=200:
    kalan = cp%200
    print(int((cp-kalan)/200),"adet 200 ₺")
    cp = kalan

if cp>=100:
    kalan = cp%100
    print(int((cp-kalan)/100),"adet 100 ₺")
    cp = kalan

if cp>=50:
    kalan = cp%50
    print(int((cp-kalan)/50),"adet 50 ₺")
    cp = kalan

if cp>=20:
    kalan = cp%20
    print(int((cp-kalan)/20),"adet 20 ₺")
    cp = kalan

if cp>=10:
    kalan = cp%10
    print(int((cp-kalan)/10),"adet 10 ₺")
    cp = kalan