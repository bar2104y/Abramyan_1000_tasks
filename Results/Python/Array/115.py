from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,30)
print(a)

b = []
for i in range(n):
    b.append(i)

for i in range(n-1):
    for j in range(n-1):
        if a[b[j]] > a[b[j+1]]:
            b[j], b[j+1] = b[j+1], b[j]

print(b)

#Для наглядности
for i in range(n):
    print(a[b[i]])

    
