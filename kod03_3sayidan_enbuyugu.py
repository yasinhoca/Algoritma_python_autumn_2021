a=int(input("a sayısını giriniz:"))
b=int(input("b sayısını giriniz:"))
c=int(input("c sayısını giriniz:"))

if a>b and a>c:
    print("En büyük sayı a = ",a)
elif b>a and b>c:
    print("En büyük sayı b = ",b)
else:
    print("En büyük sayı c = ",c)