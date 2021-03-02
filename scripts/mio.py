import random
import collections

PALOS = ['espada','corazon','rombo','trebol']
VALORES = ['as','2','3','4','5','6','7','8','9','10','jota','reina','rey']

def crear_baraja():
    baraja = [ ]
    for palos in PALOS:
        for valores in VALORES:
            baraja.append((palos,valores))
    return baraja

def obtener_mano(baraja, tamaño_mano):
    mano = random.sample(baraja, tamaño_mano)
    return mano

                      #veces que vamos a seleccionar las manos
def main(tamaño_mano, intentos):
    baraja = crear_baraja()
    manos = [ ]

    for _ in range(intentos):
        mano = random.sample(baraja, tamaño_mano)
        manos.append(mano)
    

    pares = 0

    for mano in manos:
        valores = [ ]
        for carta in mano:
            valores.append(carta[1])
        
        counter = dict(collections.Counter(valores))
    

        for val in counter.values():
            if val == 2:
                pares += 1

                break

    probabilidad_par = pares / intentos
    return f'la probabilidad de encontrar un par es de {probabilidad_par}'
    


if __name__ == '__main__':
    baraja = crear_baraja()
    print(main(5,100))