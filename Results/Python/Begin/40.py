print("A1*x + B1*y = C1")
print("A2*x + B2*y = C2")

a1 = int(input("A1: "))
b1 = int(input("B1: "))
c1 = int(input("C1: "))
print("..............")
a2 = int(input("A2: "))
b2 = int(input("B2: "))
c2 = int(input("C2: "))

d = a1*b2 - a2*b1
x = (c1*b2 - c2*b1)/d
y = (a1*c2 - a2*c1)/d

print("Solution: ( " + str(x) + " ; " + str(y) + " ).")