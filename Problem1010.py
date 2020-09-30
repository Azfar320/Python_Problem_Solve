#Simple_Calculate
A1,B1,C1 = input("").split()
A2,B2,C2 = input("").split()


a1 = int(A1)
b1 = int(B1)
c1 = float(C1)

a2 = int(A2)
b2 = int(B2)
c2 = float(C2)


total_Price = float((b1*c1)+(b2*c2))


print("VALOR A PAGAR: R$ %.2f"%total_Price)

