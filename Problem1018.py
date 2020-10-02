#Bank_Notes


Integer_Value = int(input(""))

print("%d"%Integer_Value,end="\n")
a = int(Integer_Value/100)
print("%d nota(s) de R$ 100,00"%a,end="\n")


b = (Integer_Value%100)
b1 = int(b/50)
print("%d nota(s) de R$ 50,00"%b1,end="\n")

c = b%50
c1 = int(c/20)
print("%d nota(s) de R$ 20,00"%c1,end="\n")

d = c%20
d1 = int(d/10)
print("%d nota(s) de R$ 10,00"%d1,end="\n")

e = d%10
e1 = int(e/5)
print("%d nota(s) de R$ 5,00"%e1,end="\n")

f = e%5
f1 = int(f/2)
print("%d nota(s) de R$ 2,00"%f1,end="\n")

g = f%2
g1 = int(g/1)
print("%d nota(s) de R$ 1,00"%g1,end="\n")