from genarr import genRandomArr
n = int(input("N: "))
k = int(input("K: "))

a = genRandomArr(n,0,5)
print(a)

b,c = [],[]

i = 0
cnt = 1
while i < len(a)-1:
    if a[i] == a[i+1]:
        cnt += 1
    else:
        if cnt == k:
            for j in range(k):
                a.insert(i,a[i])
            i += k

        cnt = 1
    i += 1

if cnt == k:
    for j in range(k):
        a.insert(len(a)-1,a[len(a)-1])
    
print(a)