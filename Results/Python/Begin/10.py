import math
a = int(input("A: "))
b = int(input("B: "))

s = str( a * a + b * b )
r = str( a * a - (b *b) )
p = str( a*a * b*b )
c = str( a*a / b*b)

print( "Sum: " + s)
print( "Raz: " + r)
print( "Pro: " + p)
print( "Cha: " + c)
