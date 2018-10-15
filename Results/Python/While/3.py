print("A>B")
n = int(input("N: "))
k = int(input("K: "))

r = 0

while n>=k:
	n -= k
	r+=1

print("N/K=",k,"*",r,"+",n)
