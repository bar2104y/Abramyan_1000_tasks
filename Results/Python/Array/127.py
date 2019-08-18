from genarr import genRandomArr
n = int(input("N: "))
l = int(input("L: "))

a = genRandomArr(n,0,3)
a = [1, 1, 2, 0, 2, 2, 2, 3, 3, 3]
print(a)

i,cnt, li = 0,1, 0
while i < len(a)-1:
    if a[i] == a[i+1]:
        cnt += 1
    else:
        if cnt > l:
            for j in range(cnt):
                a.pop(li)
            a.insert(li, 0)
            i = i - cnt +1
        cnt = 1
        li = i+1
    i += 1

if cnt > l:
    for j in range(cnt):
        a.pop(li)
    a.insert(li, 0)

print(a)