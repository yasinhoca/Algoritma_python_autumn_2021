# ASCII

print(chr(65))
print(ord('A'))

print(chr(97))
print(ord('h'))

import random
s = ""
for i in range(5): #rastgele 5 harfli string uretelim
    s += chr(random.randint(65,90))

print(s)