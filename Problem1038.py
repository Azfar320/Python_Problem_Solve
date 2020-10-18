#Snack

X,Y = input().split()

x = int(X)
y = int(Y)


if x==1:
    price = 4*y
elif x==2:
    price = 4.50*y
elif x==3:
    price = 5.00*y
elif x==4:
    price = 2.00*y
elif x==5:
    price = 1.50*y


print("Total: R$ %.2f"%price)