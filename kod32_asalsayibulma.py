#kendisine gönderilen sayı asal ise true
#değilse false döndüren bir fonksiyon yazınız

def asalMi(s):
    bolensayac=0
    for i in range(2,s):
        if s%i==0:
            bolensayac+=1
    if bolensayac>0:
        return False
    else:
        return True

s = int(input("Bir sayı giriniz:"))

if asalMi(s):
    print("Girdiğiniz sayı asaldır.")
else:
    print("Girdiğiniz sayı asal değildir.")

