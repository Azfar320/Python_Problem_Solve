Seconds = int(input(""))

sec = (Seconds%60)

min1 =int(Seconds/60)

if min1 >= 60:
    min = int(min1%60)
    hrs = int(min1/60)
else:
    min = min1
    hrs = 0

print("%d:"%hrs,"%d:"%min,"%d"%sec)