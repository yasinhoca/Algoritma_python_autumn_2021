#kullanıcıdan büyük harf ingiliz alfabesi ile
#ismini alıp
#ismindeki harflerin sayısal karşığını fonksiyon ile bulalım

isim = input("İsminizi giriniz")

def asciiDonusum(isim):
    for i in isim:
        print(ord(i),"-")

asciiDonusum(isim)