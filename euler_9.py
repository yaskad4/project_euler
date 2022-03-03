# Special Pythagorean triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time
start = time.time()
# codigo

a=1
booleano = True
while booleano:
    for b in range(1,1001):
        a2 = a**2
        b2 = b**2
        c = 1000-(a+b)
        c2 = c**2
        if (a2+b2)==c2:
            producto = a*b*c
            print(a,b,c)
            print(producto)
            booleano = False
    a+=1

# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")