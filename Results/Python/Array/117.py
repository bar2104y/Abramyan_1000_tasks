from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,2,5)
print(a)

a.insert(0,0)
i = 1
while i < len(a)-1:
    if a[i] != a[i+1]:
        a.insert(i+1,0)
        i += 1
    i += 1

print(a)