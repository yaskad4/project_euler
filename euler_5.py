# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import time
start = time.time()
# codigo

def es_divisible(x):
    if x%20==0 and x%19==0 and x%18==0 and x%17==0 and x%16==0 and x%15==0 and x%14==0 and x%13==0 and x%12==0 and x%11==0 :
        return True
    else:
        return False

num = 20
contador = 1
booleano = True

while booleano:
    numero = num * contador
    if es_divisible(numero):
        print(numero)
        booleano = False
    contador += 1

# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")