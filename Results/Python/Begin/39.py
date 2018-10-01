import math
print("A * x^2 + B*x + C = 0")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

d = b*b - (4*a*c)
if d < 0:
    print("No solutions")
else:
    x = (0-b - math.sqrt(d))/(a*2)
    print("X1 = " + str(x))
    x = (0-b + math.sqrt(d))/(a*2)
    print("X1 = " + str(x))