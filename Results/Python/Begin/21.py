import math
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
print("")
x2 = int(input("X2: "))
y2 = int(input("Y2: "))
print("")
x3 = int(input("X3: "))
y3 = int(input("Y3: "))

a = math.sqrt( (x1-x2) ** 2 + (y1-y2) ** 2 )
b = math.sqrt( (x2-x3) ** 2 + (y2-y3) ** 2 )
c = math.sqrt( (x1-x3) ** 2 + (y1-y3) ** 2 )
p = (a + b + c) / 2

s = math.sqrt( p * (p-a) * (p-b) * (p-c) )

print("S = " + str(s) )