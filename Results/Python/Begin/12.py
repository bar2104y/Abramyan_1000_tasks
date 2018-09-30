import math
a = int(input("A: "))
b = int(input("B: "))

c = math.sqrt( a*a + b*b )
p = str( a + b + c )
c = str( c )

print( "C = " + c )
print( "P = " + p )