
num_filas = int(input("Ingrese el número de filas para el triángulo rectángulo: "))


for i in range(1, num_filas + 1):

    print(' '.join(str(j) for j in range(1, i + 1)))
