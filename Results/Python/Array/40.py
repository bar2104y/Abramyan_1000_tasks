from genarr import genRandomArr

n = int(input("N: "))
r = int(input("R: "))

a = genRandomArr(n)
print(a)

l = a[0]
m = abs(a[0]-r)

for i in range(1,n):
    if abs(a[i] -r) < m:
        m = abs(a[i] -r)
        l = a[i]

print(l)