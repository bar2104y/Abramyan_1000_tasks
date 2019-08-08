from genarr import genRandomArr

n = int(input("N: "))

m = 0
a = genRandomArr(n)
print(a)

l1,l2 = a[0], a[1]

s = 0

for i in range(1,n):
    if a[i-1] + a[i] > m:
        m = a[i-1] + a[i]
        l1,l2 = a[i-1], a[i]

print(l1,l2)