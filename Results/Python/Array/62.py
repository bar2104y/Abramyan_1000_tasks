from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,-10,10)
print(a)

b,c = [],[]
for i in range(n):
    if a[i] > 0: b.append(a[i])
    elif a[i] < 0: c.append(a[i])

print(len(b), b)
print(len(c), c)