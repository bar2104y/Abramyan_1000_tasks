import math
a = int(input("A: "))
b = int(input("B: "))

s = str( a + b )
r = str( math.fabs( a - b ) )
p = str( math.fabs( a * b ) )
c = str( math.fabs( a / b ) )

print( "Sum: " + s)
print( "Raz: " + r)
print( "Pro: " + p)
print( "Cha: " + c)
