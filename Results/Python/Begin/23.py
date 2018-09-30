a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

d = a
a = str(c)
c = str(b)
b = str(d)

print("A = " + a)
print("B = " + b)
print("C = " + c)