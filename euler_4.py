# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


import time
start = time.time()
# codigo

a = 999
b = 999
mayor = 0

def es_palindromo(cadenaX):
    cadenaInv = ""
    for letra in cadenaX:
        cadenaInv = letra + cadenaInv
    if cadenaX == cadenaInv:
        return True
    else:
        return False

while b > 99:
    while a > 99:
        multiplico = a * b
        cadena = str(multiplico)
        if es_palindromo(cadena):
            if mayor < multiplico:
                mayor = multiplico
        a-=1
    b-=1
    a = 999

print (mayor)

# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")