fibo = [0,1]

for i in range(28):
    fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])

print(fibo)
