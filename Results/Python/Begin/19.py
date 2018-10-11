import math
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
print("")
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

a = math.fabs( x1 - x2 )
b = math.fabs( y1 - y2 )

p = 2 * ( a + b )
s = a* b

print( "P =",p) )
print( "S =",s )