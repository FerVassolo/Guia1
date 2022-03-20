"""Diseñe e implemente la clase Point2D, la cual debe representar un punto en el espacio
Cartesiano de dos dimensiones. Debe contar con los siguientes métodos:
getDistance(point): que indique la distancia que existe con el punto destino.
add(point): que devuelva un nuevo punto la suma del punto original y el argumento.
getX() : devuelve la coordenada en X
getY(): devuelve la coordenada en Y
Defina el método de clase getDistanceToOrigin(point) que devuelve la distancia entre un punto y el origen de coordenadas (0,0).
Defina el atributo de clase maxDistanceToOrigin, el cual indica la máxima distancia que existe
 entre el origen de coordenadas y cualquier punto creado a partir de la clase Point2D.
Finalmente, cree 3 objetos diferentes de la clase Point2D, con diferentes valores para las
coordenadas cartesianas x y. Muestre por pantalla cual es la máxima distancia calculada al
origen de coordenadas, a partir de los 3 puntos creados previamente.

Puede utilizar la funciones:
pow(x, y) : eleva el número x a la potencia y.
math.sqrt(x): devuelve la raíz cuadrada de x.

"""
import math

class Point2D:

    maxDistanceToOrigin = []

    def __init__(self, point):
        self.point = point
        self.maxDistanceToOrigin.append(self)

    def getDistance(self, punto):
        self.punto = punto
        #tengo dos puntos, la distancia de ambos es terorema de pitagoras.
        # C1 es la diferencia en el eje X y C2 en el eje Y
        self.distancia = math.sqrt(math.pow(self.point[0] - self.punto[0], 2) + math.pow(self.point[1] - self.punto[1], 2))
        return self.distancia

    def addPoint(self, punto):
        self.punto = punto
        self.resultado = self.point[0] + self.punto[0], self.point[1] + self.punto[1]
        return self.resultado

    def getX(self):
        return self.point[0]

    def getY(self):
        return self.point[1]

    def getDistanceToOrigin(self):
        self.origen = (0, 0)
        return self.getDistance(self.origen)


