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
    for i in range(mii+1, mai):
        a[i] = 0
else:
    for i in range(mai+1, mii):
        a[i] = 0


print(a)