from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,3)
a = [1, 1, 2, 0, 2, 2, 2, 3, 3, 3]
print(a)

i,cnt,l, li = 0,1,0, 0
while i < len(a)-1:
    if a[i] == a[i+1]:
        cnt += 1
    else:
        if cnt >= l:
            mi,l = li, cnt
        cnt = 1
        li = i+1
    i += 1

    
if cnt >= l:
    mi,l = li, cnt

i,cnt, li = 0,1,0
while i < len(a)-1:
    if a[i] == a[i+1]:
        cnt += 1
    else:
        if cnt == l:
            a.insert(i,a[i])
        cnt = 1
        li = i+1
    i += 1

    
if cnt == l:
    a.insert(li, a[i])

print(a)