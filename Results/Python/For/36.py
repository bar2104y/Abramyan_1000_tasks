n = int(input("N: "))
k = int(input("K: "))

s = 0

for i in range(1,n+1):
    s += i**k

print(s)