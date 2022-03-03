# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

import time
start = time.time()  # estas 2 primeras lineas y las 3 ultimas son para determinar el tiempo de ejecucion.

# codigo
suma = 0
contador = 1
while contador < 1000:
    if (contador % 3 == 0) or (contador % 5 == 0):
        suma += contador
    contador += 1
    
print (suma)
# final del codigo

end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")

