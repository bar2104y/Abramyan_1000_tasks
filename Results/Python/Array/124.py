from genarr import genRandomArr
n = int(input("N: "))
k = int(input("K: "))

a = genRandomArr(n,0,3)
print(a)

b = []
i = len(a)-1
cntl= 1
l = a[i]
while a[i] == a[i-1]:
    cntl += 1
    a.pop(i)
a.pop(i)

i = 0
cnt = 0
#Поиск серии K
while cnt < k and i < len(a):
    if a[i] != a[i+1]:
        cnt += 1
    i += 1
#В i первый элемент серии K

a.append(a[i])
while a[i+1] == a[i]:
    a.append(a[i])
    a.pop(i)
a.pop(i)

for j in range(cntl):
    a.insert(i,l)

print(a)