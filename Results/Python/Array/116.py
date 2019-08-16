from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

b,c = [],[]

i = 0
cnt = 1
while i < n-1:
    if a[i] == a[i+1]:
        cnt += 1
    else:
        b.append(cnt)
        c.append(a[i])
        cnt = 1
    i += 1
print("B", b)
print("C", c)