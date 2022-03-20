"""Implemente la clase Circle, que esté definida cómo un centro y un radio. De tal manera
que permita consultar su centro, su área e indicar su un punto está incluído en su área:
center() : obtiene el centro del círculo
area(): obtiene el área del círculo
contains(point): devuelve True/False si el punto está contenido.
perimeter(): devuelve el perímetro del círculo. --> dos por pi por radio
Puede utilizar la constante π haciendo uso de: math.pi
"""
import math

class Circle:

    def __init__(self, centro, radio):
        self.centro = centro #como lista
        self.radio = radio

    def center(self):
        return self.centro

    def area(self):
        return math.pi * pow(self.radio, 2)

    def contains(self, point):
        self.point = point

        if self.centro[0] - self.radio < self.point[0] < self.centro[0] + self.radio:
            if self.centro[1] - self.radio < self.point[1] < self.centro[1] + self.radio:
                return True
            else:
                return False
        else:
            return False

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __repr__(self):
        return self.centro

    def __str__(self):
        return "Centro del circulo: " + self.centro.__repr__() + "\nArea: " + str(self.area())\
            + "\nPerimetro: " + str(self.perimetro())






