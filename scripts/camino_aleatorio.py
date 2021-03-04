from borracho import Borracho_tradicional
from campo import Campo
from coordenada import Coordenada


def caminata(campo, borracho, pasos):
    #obtiene la posicion en la que se encuentra el borracho
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)
    #el metodo distancia lo tenemos en la clase Coordenada
    return inicio.distancia(campo.obtener_coordenada(borracho))

#añadir return a la funcion simular_caminata
def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    #aqui definimos al tipo de borracho, al objeto, pero
    #lo hacemos mediante un parametro
    borracho = tipo_de_borracho(nombre = 'Fernando')
    #en origen defino el objeto con la clase Coordenada
    origen = Coordenada(0, 0)

    #esta lista va a guardar las distancias que recorremos
    #en cada simulacion
    distancias = []


    #el _ significa que no vamos a usar la variable
    for _ in range(numero_de_intentos):
        #creamos un objeto con la clase Campo
        campo = Campo()
        #usamos el metodo de la clase Campo para poner al 
        #borracho en el origen (0,0)
        campo.añadir_borracho(tipo_de_borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        #vamos a añadir a la lista distancias la simulacion de la caminata
        distancias.append(round(simulacion_caminata, 1))#con esta funcion redondeamos a numero enteros
    return distancias



#esta funcion es la que va a hacer la simulacion
def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):


    #por cada paso en la distancia de la caminata
    for pasos in distancias_de_caminata:
        #nos retorna una lista de que distancias se recorrieron en esta simulacion
        distancia = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)#la funcion retorna la distancia que se recorrio
        distancia_media = round(sum(distancia)/len(distancia), 4)
        distancia_maxima = max(distancia)
        distancia_minima = min(distancia)
        print(f'{tipo_de_borracho.__name__} tuvo una caminata aleatorio de {pasos}')
        print(f'la distancia media es {distancia_media}, la distancia maxima es {distancia_maxima} y la distancia minima es {distancia_minima}')





#el entry point quiere decir que si el archivo se ejecuta
#directamente desde la terminal, entonces que se ejecute
# el codigo que hay debajo 
if __name__ == '__main__':
    #numero de pasos de la simulacion
    distancias_de_caminata = [10, 100, 1000, 10000]

    #numero de veces que vamos a ejecutar la simulaicon
    numero_de_intentos = 100
                                                   #tipo de borracho
    main(distancias_de_caminata, numero_de_intentos, Borracho_tradicional)