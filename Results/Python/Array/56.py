from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)
b = []

i = 3
while i < n:
    b.append(a[i])
    i += 3
print(b)