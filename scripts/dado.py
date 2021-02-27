import random

class Dado:
    def __init__(self, lado_1, lado_2, lado_3, lado_4, lado_5, lado_6):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
        self.lado_4 = lado_4
        self.lado_5 = lado_5
        self.lado_6 = lado_6


    def lado(self, simulaciones):
        paso = 1
        resultados = [ ]
        while paso <= simulaciones:
            
            
            resultados.append(random.choice([self.lado_1,self.lado_2,self.lado_3,self.lado_4,self.lado_5,self.lado_6, self.lado_1 + self.lado_1,self.lado_1 + self.lado_2,self.lado_1 + self.lado_3,self.lado_1 + self.lado_4,self.lado_1 + self.lado_5,self.lado_1 + self.lado_6,self.lado_2 + self.lado_1,self.lado_2 + self.lado_2,self.lado_2 + self.lado_3,self.lado_2 + self.lado_4,self.lado_2 + self.lado_5,self.lado_2 + self.lado_6,self.lado_3 + self.lado_1,self.lado_3 + self.lado_2,self.lado_3 + self.lado_3,self.lado_3 + self.lado_4,self.lado_3 + self.lado_5,self.lado_3 + self.lado_6,self.lado_4 + self.lado_1,self.lado_4 + self.lado_2,self.lado_4 + self.lado_3,self.lado_4 + self.lado_4,self.lado_4 + self.lado_5,self.lado_4 + self.lado_6,self.lado_5 + self.lado_1,self.lado_5 + self.lado_2,self.lado_5 + self.lado_3,self.lado_5 + self.lado_4,self.lado_5 + self.lado_5,self.lado_5 + self.lado_6,self.lado_6 + self.lado_1,self.lado_6 + self.lado_2,self.lado_6 + self.lado_3,self.lado_6 + self.lado_4,self.lado_6 + self.lado_5,self.lado_6 + self.lado_6]))
            cara_1 = resultados.count(1)
            cara_2 = resultados.count(2)
            cara_3 = resultados.count(3)
            cara_4 = resultados.count(4)
            cara_5 = resultados.count(5)
            cara_6 = resultados.count(6)
            cara_12 = resultados.count(12)
            paso += 1
        print(f'El lado {self.lado_1} ha aparecido {cara_1}')
        print(f'El lado {self.lado_2} ha aparecido {cara_2}')
        print(f'El lado {self.lado_3} ha aparecido {cara_3}')
        print(f'El lado {self.lado_4} ha aparecido {cara_4}')
        print(f'El lado {self.lado_5} ha aparecido {cara_5}')
        print(f'El lado {self.lado_6} ha aparecido {cara_6}')
        print(f'El lado 12 ha aparecido {cara_12}')

        probabilidad_1 = cara_1 / simulaciones
        print(f'la probabilidad de que {self.lado_1} salga es de {probabilidad_1}')
        #print(resultados)
        probabilidad_12 = cara_12 / simulaciones
        print(f'la probabilidad de que 12 salga es de {probabilidad_12}') 
        return resultados, cara_1,cara_2,cara_3,cara_4,cara_5,cara_6


if __name__ == '__main__':
    simulaciones = int(input('cuantas veces quieres simular el lanzamineto?? '))
    dado = Dado(1,2,3,4,5,6)
    dado.lado(simulaciones)