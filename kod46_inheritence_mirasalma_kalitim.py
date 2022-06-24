#Inheritence
#miras alma - kalıtım

class kus:       # super sınıf - ana sınıf
    tur_ad=""
    kus_ad=""

    def isimYaz(self):
        print("Tür adı :",self.tur_ad)
        print("Kuş ismi",self.kus_ad)

class yirtici(kus):   #subclass - alt sınıf
    kanat_uzunlugu = "0"
    agirlik = "0"

class kartal(yirtici):
    alt_tur = ""


anadolu_kartali = kartal()
anadolu_kartali.kus_ad #dedesinden miras
anadolu_kartali.kanat_uzunlugu #babasından miras


