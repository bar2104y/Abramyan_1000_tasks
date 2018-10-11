import math
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

bc = math.fabs( c - b )
ac = math.fabs( a - c )
s = ac + bc

print("AC =",ac)
print("BC =",bc)
print("AC + BC =",s)