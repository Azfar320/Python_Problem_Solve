from math import *

N = float(input(""))


#NOTAS
A = int(N/100)   #100 Notes
A1 = (N%100)

B = int(A1/50)  #50 notes
B1 = (A1%50)

C = int(B1/20)   #20 notes
C1 = B1%20

D = int(C1/10)   #10 notes
D1 = C1%10

E = int(D1/5)    #5 notes
E1 = D1%5

F = int(E1/2)    #2 notes
F1 = int(E1%2)

#MOEDAS

e=N*100
b=(int(e))
m=b%100
n=int(m/50)
o=m%50
p=int(o/25)
q=o%25
r=int(q/10)
s=q%10
t=int(s/5)
u=s%5


print("NOTAS:")
print("%d nota(s) de R$ 100.00"%A)
print("%d nota(s) de R$ 50.00"%B)
print("%d nota(s) de R$ 20.00"%C)
print("%d nota(s) de R$ 10.00"%D)
print("%d nota(s) de R$ 5.00"%E)
print("%d nota(s) de R$ 2.00"%F)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%F1)
print("%d moeda(s) de R$ 0.50"%n)
print("%d moeda(s) de R$ 0.25"%p)
print("%d moeda(s) de R$ 0.10"%r)
print("%d moeda(s) de R$ 0.05"%t)
print("%d moeda(s) de R$ 0.01"%u)


