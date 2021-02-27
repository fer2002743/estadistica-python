import random 

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = [ ]

    for _ in range(len(secuencia_de_tiros)):
        tiro = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append(tiro)
    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = [ ]
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    #ahora calculamos las probabilidades
    tiros_con_uno = 1
    for tiro in tiros:
        if 1 in tiros:
            tiros_con_uno += 1                   #nuero de veces que genero la simulacion
    probabilidad_tiros_con_uno = tiros_con_uno / numero_de_intentos
    print(f'la probabilidad de que salga uno tirando el dado {numero_de_intentos} veces es {probabilidad_tiros_con_uno}')
    #print(f'')


if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas veces quieres tirar el dado? '))
    numero_de_intentos = int(input('cuantas veces quieres generar la simulacion '))

    main(numero_de_tiros, numero_de_intentos)