from genarr import genRandomArr

n = int(input("N: "))
r = int(input("R: "))

a = genRandomArr(n)
print(a)

l1, l2 = a[0], a[1]
m = abs(a[0]+a[1]-r)

for i in range(1,n):
    if abs(a[i]+a[i-1] -r) < m:
        m = abs(a[i]+a[i-1]-r)
        l1, l2 = a[i-1], a[i]

print(l1,l2)