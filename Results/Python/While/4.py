print("(N = 3^k)")
n = int(input("N: "))

while n % 3 == 0:
	n /= 3

if n == 1:
	print(True)
else:
	print(False)
