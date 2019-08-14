from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

i = 0
while i < n:
    a[i],a[i+1] = a[i+1], a[i]
    i += 2

print(a)