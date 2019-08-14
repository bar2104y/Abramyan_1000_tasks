from genarr import genRandomArr
n = int(input("N: "))
k = int(input("K: "))

a = genRandomArr(n)
print(a)

k = a[k]

for i in range(n):
    a[i] += k

print(a)