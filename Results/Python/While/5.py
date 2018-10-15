print("N = 2^k")
n = int(input("N: "))

r = 0

while n != 1:
	n /= 2
	r += 1

print("k =",r)
