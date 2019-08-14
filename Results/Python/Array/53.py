from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
b = genRandomArr(n)
print("Массив A:", a)
print("Массив B:", b)

c = []

for i in range(n):
    c.append(max(a[i],b[i]))

print("Массив C:", c)