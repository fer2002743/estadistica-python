#con esta libreria voy a intentar solucinar el problema 
#de python de que he llegado al maximo limite de recusrividad
import sys


# def fibonacci_recursivo(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

#ahora voy a optimizar el problema mediante la memorizacion:

def fibonacci_dinamico(n, memorizacion = {}):
    if n == 0 or n == 1:
        return 1

    else:
        try:
            return memorizacion[n]
        except KeyError:
            #si no tenemos el valor guardado en memorizacion hacemos esto
            resultado = fibonacci_dinamico(n-1, memorizacion) + fibonacci_dinamico(n-2, memorizacion)
            memorizacion[n] = resultado
            return resultado




if __name__ == '__main__':
    #este es el limete de recurividad que yo establezco
    sys.setrecursionlimit(1000000000)
    n = int(input('de que numero queires hacer la sucesion? '))
    resultado = fibonacci_dinamico(n)
    print(resultado)