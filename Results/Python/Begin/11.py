import math
a = int(input("A: "))
b = int(input("B: "))

s = math.fabs( a + b )
r = math.fabs( a - b )
p = math.fabs( a * b )
c = math.fabs( a / b )

print( "Sum:", s)
print( "Raz:", r)
print( "Pro:", p)
print( "Cha:", c)
