def media(valores, cantida_elementos):
    suma = sum(valores)
    media = suma / cantida_elementos
    return media

if __name__ == '__main__':
    valores = [ ]

    print('Por favor introduce los elementos cuya media quieres calcular, pero si deseas salir escribe 1989')

    while True:
        numeros = int(input('introduce digito: '))
        valores.append(numeros)
        if numeros == 1989:
            valores.remove(1989)
            break
        
    
    
    cantidad_elementos = len(valores)
    print(f'la media de los valores introducidos es {media(valores, cantidad_elementos)}')

