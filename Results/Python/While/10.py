n = int(input("N: "))

k = 0

while 3**k < n:
	k += 1

print("K =",k-1)