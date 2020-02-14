import math

e = 27
d = 3
n = 15
m = 12

c = 12
print("Mensaje a cifrar: ", c)

for i in range(1, e):
    c = (c*m) % n
print("Cifrado: ", c)

j = c
for i in range(1, d):
    j = (j*c) % n
print("Descifrado: ", j)
