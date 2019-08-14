from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

f = False
d = 0

i = n-1

while i >= 0:
    if a[i]%2 == 1:
        if not f:
            f = True
            d = a[i]
            a[i] *= 2
        else:
            a[i] += d
    i -= 1
print(a)