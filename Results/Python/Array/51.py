from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
b = genRandomArr(n)
print("Массив A:", a)
print("Массив B:", b)

for i in range(n):
    a[i],b[i] = b[i],a[i]
    #tmp = a[i]
    #a[i] = b[i]
    #b[i] = tmp

print("Массив A:", a)
print("Массив B:", b)