import random
import math

def media(X):
    return sum(X) / len(X)

def varianza(X):
    mu = media(X)

    acumulador = 0
    for x in X:
        acumulador += (x - mu) ** 2
    return acumulador / len(X)

def desviacion_estandar(X):
    return (varianza(X)) ** 0.5

if __name__ == '__main__':
    X = [random.randint(9, 12) for i in range(20)]
    mu = media(X)
    var = varianza(X)
    desv = desviacion_estandar(X)

    print(X)
    print(f'la media es {mu}')
    print(f'la varianza es {var}')
    print(f'la desviacion estander en {desv}')