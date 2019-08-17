from genarr import genRandomArr
n = int(input("N: "))
k = int(input("K: "))

a = genRandomArr(n,0,3)
print(a)

i = 0
cnt = 0
while cnt != k and i < len(a):
    if a[i] != a[i+1]:
        cnt += 1
    i += 1

tmp = a[i]

while a[i] == tmp:
    a.pop(i)

print(a)