# Sum square difference

# The sum of the squares of the first ten natural numbers is,

# The square of the sum of the first ten natural numbers is,

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


import time
start = time.time()
# codigo

limite = 100
suma = 0
sumaCuadrado = 0
cuadradoSuma = 0

for i in range(1, limite+1):
    suma = suma + i 
    cuadrado = i ** 2
    sumaCuadrado += cuadrado

cuadradoSuma = suma ** 2
resultado = cuadradoSuma - sumaCuadrado

print(resultado)

# final
end = time.time()
tiempoTotal = end - start
print("TIEMPO DE EJECUCION: ", round(tiempoTotal,3),"segundos")