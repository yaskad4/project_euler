# Summation of primes

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


import time
start = time.time()
# codigo

def suma_primos(n):
    suma = 2
    marcados = [0]*n
    valor = 3
    while valor < n:
        if marcados[valor]==0:
            suma+=valor
            i = valor
            while i < n:
                marcados[i]=1
                i+=valor 
        valor+=2
    return suma

limite = 2000000
print(suma_primos(limite))


# ******************************************
# ESTE ES EL PRIMER CODIGO QUE UTILIZAMOS:
# ******************************************
# def es_primo(a):
#     for i in range(2,int(a**0.5)+1):
#         if a % i == 0:
#             return False
#     return True
# limite = 2000000
# suma = 0
# i = 2
# while i <= limite:
#     if es_primo(i):
#         suma+=i
#     i+=1
# print(suma)



# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")