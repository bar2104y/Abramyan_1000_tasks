#Первая == нулевая
# настоящие программисты считают с нуля, поэтому если уж очень нужно, то можно раскомментить  нужные строки
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

# i -= 1 костыль для нормального счету
tmp = a[i]
cnt = 0
b = []

while a[i] == tmp:
    cnt += 1
    b.append(a[i])
    a[i] = a[0]
    i +=1

tmp = a[0]
i = 0

while a[i] == tmp:
    a.pop(i)

a = b+a

print(a)