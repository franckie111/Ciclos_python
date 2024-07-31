def fibonacci(n):

    serie = []
    a, b = 0, 1
    
    while len(serie) < n:
        serie.append(a)
        a, b = b, a + b
    
    return serie

def suma_fibonacci(serie):
    return sum(serie)


n = int(input("Ingrese el número de términos de la serie de Fibonacci: "))


serie = fibonacci(n)


suma = suma_fibonacci(serie)


print(f"Los primeros {n} términos de la serie de Fibonacci son: {serie}")
print(f"La suma de estos términos es: {suma}")
