from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

f = False
d = 0

for i in range(n):
    if a[i]%2 == 0:
        if not f:
            f = True
            d = a[i]
            a[i] *= 2
        else:
            a[i] += d
print(a)