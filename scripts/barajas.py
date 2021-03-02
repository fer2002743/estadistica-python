import random
import collections

#generar barajas, las variables las nombre en mayusculas 
#porque es una convencion
PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

#funcion para generar la baraja

def crear_baraja():
    barajas = [ ]

    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))

    return barajas

#ahora creamos una funcion para obtener una mano
def obtener_mano(barajas, tamaño_mano):
    #la funcion random.sample escoge una muestra aleatorio de barajas
    #y el tamaño de la mano le indica cuantas barajas vamos
    #a obtener
    mano = random.sample(barajas, tamaño_mano)
    return mano
#funcion para encontrar las probabilidadeas de los pares en
#una barja
def par(valores_acumulados):

    for val in valores_acumulados:
        if val == 2:
            return 1
        #retorna cero al finalizar el ciclo
        return 0

def main(tamaño_mano, intentos):
    #creamos una baraja
    baraja = crear_baraja()
    #guarda todas las manos que obtengamos en la simulacion
    manos = [ ]
    for _ in range(intentos):
        mano = obtener_mano(baraja, tamaño_mano)
        manos.append(mano)


    #ahora vamos a calcular la probabilidad de que nos salga
    #un par dentro de una mano de cualquier tamaño
    # pares = 0
    
    for mano in manos:
        valores = [ ]
        for carta in mano:
            valores.append(carta[1])

            counter = dict(collections.Counter(valores))
        for val in counter.values():
            #es exactamente dos porque si una carta aparece 
            #exactamente dos veces es un par
            if val == 2:
                pares += 1
                #si encontramos un par ya dejamos de buscar
                #porque solo queremos encontrar dos
                break
    probabilidad_pares = pares / intentos
    return f'la probabilidad de encontrar un par dentro de una mano es de {tamaño_mano} barajs es {probabilidad_pares}'


if __name__ == '__main__':
    barajas = crear_baraja()
    tamaño_mano = int(input('de que tamaño quieres que sea el tamaño de la mano?? '))
    intentos = int(input('cauntas veces quieres generar la simulaicon?? '))
    #mano = obtener_mano(barajas, tamaño_mano)
    print(main(tamaño_mano, intentos))