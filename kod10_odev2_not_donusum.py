v = int(input("vize notunuzu giriniz:"))
f = int(input("final notunuzu giriniz:"))

o = (v*0.4)+(f*0.6)
print("Ortalamanız:",o)

if o>=90 and o<=100:
    print("AA")
elif o>=85 and o<90:
    print("BA")
elif o>=75 and o<85:
    print("BB")
elif o>=70 and o<75:
    print("CB")
elif o>=60 and o<70:
    print("CC")
elif o>=55 and o<60:
    print("DC")
elif o>=50 and o<55:
    print("DD")
else:
    print("FF")