from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)
mi,ma = 1001,0


for i in range(n):
    if a[i] < mi:
        mi = a[i]
        mii = i
    if a[i] > ma:
        ma = a[i]
        mai = i

a[mai] = mi
a[mii] = ma

print(a)