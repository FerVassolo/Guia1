from g1ej1 import BankAccount
from ej2 import Rectangle
from ej3 import Point2D
from ej4 import Circle
from ej5 import Dado

#1
print("#1")
balance = BankAccount("123")
balance.deposit(400)
balance.withraw(300)
print(balance.__str__())
print("\n")

#2
print("#2")
rectangulo1 = Rectangle(10, 5)
print(rectangulo1.calcularArea())
print("\n")

#3
print("#3")
punto = Point2D([2,1])
punto2 = Point2D([3,3])
punto3 = Point2D([4,3])
print(punto.getDistance([2,2]))
print(punto.addPoint([2,2]))
print(punto.getDistanceToOrigin())

resultado = 0
for punto in Point2D.maxDistanceToOrigin:
    if punto.getDistanceToOrigin() > resultado:
        resultado = punto.getDistanceToOrigin()
print(resultado)
print("\n")

#4
print("#4")
circulo1 = Circle([23,9], 10)
print(circulo1.perimetro())
print(circulo1.contains([0, 1]))
print(circulo1.__str__())
print("\n")

#5
print("#5")
dado1 = Dado(3)
print(dado1.__str__())
dado2 = Dado(6)
print(dado2.__str__())
