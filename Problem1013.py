#The greatest
from math import *

A1,B1,C1 = input().split()

A = int(A1)
B = int(B1)
C = int(C1)

MaiorAB = (A+B+abs(A-B))/2

greatest = (C+MaiorAB+abs(C-MaiorAB))/2

print("%d eh o maior"%greatest)