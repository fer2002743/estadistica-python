
#abstraccion de donde se encuentra el borracho en el plano
class Coordenada:


    #estas son las posiciones iniciales
    def __init__(self, x,y):
        self.x = x
        self.y = y

    #para saber cuanto nos movemos a las coordenadas iniciales
    #(self.x y self.y) le sumamos lo que nos movemos, delta_x y delta_y
    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    

    #lo usamos para saber la distancia del borracho con 
    #respecto de otro objeto
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.delta_x
        delta_y = self.y - otra_coordenada.delta_y
        return (delta_x**2 + delta_y**2)**0.5


