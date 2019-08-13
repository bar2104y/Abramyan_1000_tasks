from genarr import genRandomArr
#Самое простое решение O = n^2
n = int(input("N: "))

a = genRandomArr(n,0,10)
print(a)
b = []


for i in range(n):
    if a[i] not in b:
        b.append(a[i])

print(len(b))