import math

print( "A < C < B or B < C < A" )
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

l = math.fabs( (a-c) * (b-c) )

print("Result =",l)