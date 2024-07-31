
suma = 0
cantidad_numeros = 10


for i in range(cantidad_numeros):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    suma += numero


promedio = suma / cantidad_numeros


print(f"La suma de los 10 números es: {suma}")
print(f"El promedio de los 10 números es: {promedio:.2f}")
