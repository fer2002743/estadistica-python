import random
from varianza import desviacion_estandar


def aventar_agujas(numero_agujas):
    
    dentro_del_circulo = 0
    

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
        estimaciones_pi.append(estimacion_pi)

    media_estimados = sum(estimaciones_pi) / len(estimaciones_pi)
    sigma = desviacion_estandar(estimaciones_pi)
    return (media_estimados, sigma)


#en esta estimacion le meto una aproximacion al calculo
def estimar_pi(precision, numero_intentos):
    numero_agujas = 1000
    sigma = precision#inicializamos sigma en precision

    while  sigma >= precision/1.96:
        media, sigma = estimacion(numero_agujas, numero_intentos)
        numero_agujas *= 2
    return media



if __name__ == '__main__':
    print(estimar_pi(0.01, 10))