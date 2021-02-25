import random
from bokeh.plotting import figure, output_file, show

eje_x = [0]
eje_y = [0]

class Persona:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, x, y, nueva_x, nueva_y):
        self.x = nueva_x
        self.y = nueva_y
        return self.x, self.y

    def tipo_movimiento(self):
        movimientos = []
        movimientos.append(random.choice([0, -1, 1]))
        movimientos.append(random.choice([0, -1, 1]))
        return movimientos


def caminata(Persona, simulaicones):

    #creamos un objeto con la clase persona
    caminante = Persona(0,0)

    posicion = [(0,0)]

    paso = 1

    while paso <= simulaicones:
        


        #estas coordenadas marcan el punto de partida del caminante
        
        x = caminante.x 
        y = caminante.y


        movimientos = caminante.tipo_movimiento()
        #estas nuevas coordenadas marcan el lugar a donde ha llegado
        #el caminante

        nueva_x = x + movimientos[0]
        nueva_y = y + movimientos[1]


        if movimientos[0] == 0 and movimientos[1] == 0:
            #no ejecutamos nada
            pass
        else:
            caminante.mover(x,y,nueva_x, nueva_y)
            posicion.append((nueva_x, nueva_y))
            paso += 1
            eje_x.append(nueva_x)
            eje_y.append(nueva_y)

    return posicion 


if __name__ == '__main__':
    simulaicones = int(input('cuantas veces quieres generar la simulacion?? '))
    caminata(Persona, simulaicones)
    fig = figure()
    fig.line(eje_x,eje_y,line_width= 2)
    show(fig)