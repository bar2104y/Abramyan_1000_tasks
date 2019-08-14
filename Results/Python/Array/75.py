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

if mai > mii:
    for i in range(mii, mai+1):
        a[i] = 0
else:
    for i in range(mai, mii+1):
        a[i] = 0


print(a)