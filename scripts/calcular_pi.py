import random
from varianza import desviacion_estandar


def aventar_agujas(numero_agujas):
    dentro_del_circulo = 0
    #dentro_cuadrado = 0

    for _ in range(numero_agujas):
        #random nos retorna un valor entre cero y uno. Pero 
        #lo que queremos es obtener es uno o menos uno de forma
        #aleatoria, para ello lo que hacmeos es que lo multiplicamos 
        #de forma aletaria por uno o menos uno
        x = random.random() * random.choice([1,-1])
        y = random.random() * random.choice([1,-1])
        distancia_desde_el_centro = (x**2 + y**2)**0.5

        if distancia_desde_el_centro <= 1:
            dentro_del_circulo += 1
        # elif distancia_desde_el_centro < 1:
        #     dentro_cuadrado += 1
    return (4 * dentro_del_circulo) / numero_agujas 


                              #las veces que vamos a correr la simulacion
def estimacion(numero_agujas, numero_intentos):
    estimaciones_pi = [ ]
    for _ in range(numero_intentos):
        estimacion_pi = aventar_agujas(numero_agujas)
        estimaciones_pi.append(estimacion)

    media_estimados = sum(estimaciones_pi) / len(estimaciones_pi)
    sigma = desviacion_estandar(estimaciones_pi)
    return f'la media de realizar {numero_intentos} veces {numero_agujas} agujas tiene como media {media_estimados} con una desviacion estandar de {sigma}'



if __name__ == '__main__':
    print(aventar_agujas(10000000))