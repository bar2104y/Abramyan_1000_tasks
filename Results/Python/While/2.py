print("A>B")
a = int(input("A: "))
b = int(input("B: "))

k = 0

while a >= b:
	a -= b
	k += 1

print("A/B =", k, "*", b,"+", a)