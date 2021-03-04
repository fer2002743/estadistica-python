class Campo:
    def __init__(self):
        #definimos un diccionario para guardar las coordenadas en las que estan los borrachos
        self.coordenada_de_borrachos = {}

    
    #con esta funcion añadimos un borracho y su posicion
    #borracho sera la llave del diccionario y coordenada sera
    #el valor asociado.
    def añadir_borracho(self, borracho, coordenada):
        self.coordenada_de_borrachos[borracho] = coordenada
              #el borracho es la llave del dic, y la coordenada es el valor


    def mover_borracho(self, borracho):
        #Cuando el borracho se mueve se ejecuta el metodo
        #camina de la clase BorrachoTradicional creado en el
        #archivo borracho.py. Esta funcion nos retorna la 
        #direccion hacia la que se movio el borracho
        delta_x, delta_y = borracho.camina()

        #obtenemos coordenada actual del diccionario de coordenadas
        coordenada_actual = self.coordenada_de_borrachos[borracho]

        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)

        self.coordenada_de_borrachos[borracho] = nueva_coordenada

    #para saber donde esta un borracho despues de finalizar el programa
    def obtener_coordenada(self, borracho):
        return self.coordenada_de_borrachos[borracho]

