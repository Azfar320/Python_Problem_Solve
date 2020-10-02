#Fuel_Spent

Time_of_Travel = int(input(""))
Car_avg_Speed = int(input(""))


Total_Distance = (Time_of_Travel*Car_avg_Speed)

Amount_of_Oil = float(Total_Distance/12)


print("%.3f"%Amount_of_Oil)