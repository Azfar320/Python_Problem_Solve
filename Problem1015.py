#Distance between two points
from math import *

A1,B1 = input().split()
A2,B2 = input().split()

p1 = float(A1)
p2 = float(B1)
p3 = float(A2)
p4 = float(B2)

result = sqrt(pow((p3-p1),2)+pow((p4-p2),2))

print("%.4f"%result)