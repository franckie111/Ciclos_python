
numero = int(input("Ingrese el número para mostrar su tabla de multiplicar: "))


print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
