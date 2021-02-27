def media(valores, cantida_elementos):
    suma = sum(valores)
    media = suma / cantida_elementos
    return media

if __name__ == '__main__':
    valores = [1,2,3,4,5,6,7,8,9]
    cantidad_elementos = len(valores)
    print(f'la media de los valores es {media(valores,cantidad_elementos)}')