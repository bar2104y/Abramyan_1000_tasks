print("A^n")
a = float(input("A: "))
n = int(input("n: "))
k = 1

for i in range(1, n+1):
	if i % 2 == 0:
		k += a ** i
	else:
		k -= a ** i 

print("R = ", k)