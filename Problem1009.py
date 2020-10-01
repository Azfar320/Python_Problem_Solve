#SALARY With BONUS

SalesMan_Name = input("")
SalesMan_Salary = float(input(""))
Sold_Product = float(input(""))


Total_Salary = (SalesMan_Salary+((15*Sold_Product)/100))

print("TOTAL = R$ %.2f"%Total_Salary,end="\n")