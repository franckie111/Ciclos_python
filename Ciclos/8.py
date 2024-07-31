
num_filas = int(input("Ingrese el número de filas para la pirámide: "))


for i in range(1, num_filas + 1):

    print(' ' * (num_filas - i), end='')
    

    for j in range(1, i + 1):
        print(j, end='')
    

    print()
