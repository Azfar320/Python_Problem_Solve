#Area


from math import *
A1,B1,C1 = input("").split()
A = float(A1)
B = float(B1)
C = float(C1)
pi = 3.14159


Rectangled_Triangle_area = 0.5*(A*C)

Radius_Circle_area = pi*C*C

Traphezium_area = (((A+B)/2)*C)

Square_area = B*B

Rectangle_area = A*B


print("TRIANGULO: %.3f"%Rectangled_Triangle_area)
print("CIRCULO: %.3f"%Radius_Circle_area)
print("TRAPEZIO: %.3f"%Traphezium_area)
print("QUADRADO: %.3f"%Square_area)
print("RETANGULO: %.3f"%Rectangle_area)
