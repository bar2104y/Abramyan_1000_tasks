from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

for i in range(n-1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print(a)
