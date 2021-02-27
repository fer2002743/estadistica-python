import random

class Ruleta:
    def __init__(self, rojo, negro, cero):
        self.rojo = rojo
        self.negro = negro
        self.cero = cero

    def simulacion(self, simulaciones):
        lista = [ ]

        for _ in range(18):
            lista.append(self.rojo)

        for _ in range(18):
            lista.append(self.negro)

        lista.append(self.cero)

        #rojos = lista.count(self.rojo)
        #negros = lista.count(self.negro)
        #ceros = lista.count(self.cero)

        paso = 1
        lista_aleatoria = [ ]

        while paso <= simulaciones:
            lista_aleatoria.append(random.choice(lista))
            paso += 1

        rojo_contar = lista_aleatoria.count(self.rojo)
        probabilidad_rojo = rojo_contar / simulaciones 

        negro_contar = lista_aleatoria.count(self.negro)
        probabilidad_negro = negro_contar / simulaciones

        cero_contar = lista_aleatoria.count(self.cero)
        probabilidad_cero = cero_contar / simulaciones

        print(f'{self.rojo} ha salido {rojo_contar} veces, y su probabilidad es {probabilidad_rojo}')
        print(f'{self.negro} ha salido {negro_contar} veces, y su probabilidad es {probabilidad_negro}')
        print(f'{self.cero} ha salido {cero_contar} veces, y su probabilidad es {probabilidad_cero}')
        #print(f'en la lista hay {rojos} rojos, {negros} negros y {ceros} ceros')


if __name__ == '__main__':
    
    ruleta = Ruleta('rojo','negro','cero')
    simulaciones = int(input('cuantas veces quieres simular la simulacion?? '))
    ruleta.simulacion(simulaciones)
