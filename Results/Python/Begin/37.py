import math
v1 = int(input("V1: "))
v2 = int(input("V2: "))
s = int(input("S0:  "))
t = int(input("T:   "))

s = math.fabs(s-(t*(v1+v2)))

print("S = " + str(s) )