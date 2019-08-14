from genarr import genRandomArr
#Самое простое решение O = n^2
n = int(input("N: "))
a = genRandomArr(n,0,10)
print(a)

b=[]
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        if a[i] == a[j]:
            if a[i] not in b:
                b.append(a[i])
                cnt += 2
            else:
                cnt += 1

print(cnt)