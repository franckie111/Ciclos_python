
num_filas = int(input("Ingrese el número de filas para el patrón Z: "))


for i in range(num_filas):
    if i == 0 or i == num_filas - 1:

        print('*' * num_filas)
    else:

        print(' ' * (num_filas - i - 1) + '*')
