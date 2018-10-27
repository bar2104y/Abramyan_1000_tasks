n = int(input())
a = []
k = 0

for i in range(1, n+1):
	b = int(input())
	if b%2 != 0:
		a.append(i)
		k += 1
		
print(a)
print(k)