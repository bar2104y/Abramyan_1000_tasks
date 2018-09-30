import math
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
print("")
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

d = math.sqrt( (x1-x2) ** 2 + (y1-y2) ** 2 )
print("Dist = " + str(d) )