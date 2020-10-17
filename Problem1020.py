#Age in days

Days = int(input(""))


if Days >= 365:
    Year = int(Days/365)
    Month = ((Days%365)/30)
    Day = ((Days%365)%30)
else:
    Year = 0
    Month = int((Days/30))
    Day = Days%30

print("%d ano(s)"%Year)
print("%d mes(es)"%Month)
print("%d dia(s)"%Day)