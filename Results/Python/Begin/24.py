a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

d = c
c = a
a = b
b = d

print("A =", a)
print("B =", b)
print("C =", c)