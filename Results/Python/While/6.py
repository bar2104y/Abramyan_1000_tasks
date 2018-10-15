print("N!!")
n = int(input("N: "))

i = 0
r = n

while i <= n:
	r *= n*(n-i)
	i += 2

print("N!! =",r)