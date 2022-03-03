# Largest prime factor

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import time
start = time.time()
# codigo
def esPrimo(x):
    #casos especiales
    if (x == 0) or (x == 1):
        return False # directamente no son primos por definicion
    i = 2 # porque comenzare a iterar por el 2
    while i < (x/2):
        if x % i == 0:
            return False
        i += 1
    return True # si llegue a este punto es que el numero nunca fue divisible y por tanto es primo

#print(esPrimo(1999993))  # este se que es primo 

numero = 600851475143

if esPrimo(numero) == True:
    print(numero, " es primo.")
else:
    divisor = 2
    while (numero > divisor):
        if esPrimo(divisor):
            if numero % divisor == 0:
                numero = numero / divisor
        divisor += 1
    print("Respuesta: ", divisor)
# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")