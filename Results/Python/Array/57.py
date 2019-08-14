from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)
b = []

i = 2
while i < n:
    b.append(a[i])
    i += 2

i = 1
while i < n:
    b.append(a[i])
    i += 2
print(b)