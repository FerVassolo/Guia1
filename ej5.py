"""Diseñe e implemente una clase que permita modelar un Dado no convencional, es decir,
un dado que puede tener un número de caras distinto de seis. Cada objeto de esta clase conoce cuántos lados tiene y su valor actual.
Cuando el dado se crea, se debe especificar cuántas caras tiene.
La clase debe contener dos métodos: lanzar() para obtener un valor aleatorio entre 1 y n (el número de caras)
y obtenerValor() que muestra el valor actual del dado.
Implemente un código de prueba, considere generar dos dados y realizar las pruebas de lanzamiento de los mismos.
"""
import random


class Dado:

    def __init__(self, lados):
        self.lados = lados

    def lanzar(self):
        return random.randint(1, self.lados)

    def obtenerValor(self):
        return self.lanzar()
    def __str__(self):
        return "El dado tiene " + str(self.lados) + " lados \n" + "El lado obtenido es: " + str(self.obtenerValor())

