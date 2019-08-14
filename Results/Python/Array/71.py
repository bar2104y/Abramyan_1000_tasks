from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

h = n//2

for i in range(h):
    a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
print(a)
    