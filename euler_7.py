# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import time
start = time.time()
# codigo

def es_primo(a):
    for i in range(2,int(a**0.5)+1):         # el mas 1 es porque tiene que llegar hasta el mismo valor no al anterior
        if a%i == 0:
            return False
    return True

posicion = 1
numero = 2
while True:
    if es_primo(numero):
        if posicion == 10001:
            print(numero)
            break
        posicion+=1
    numero+=1

# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")