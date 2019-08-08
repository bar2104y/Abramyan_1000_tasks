from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr (n)
print(a)

cnt = 0
u = False
d = False

for i in range(1,n):
    if a[i] < a[i-1]:
        if not d:
            cnt += 1
            d= True
            u = False
    elif a[i] > a[i-1]:
        if not u:
            cnt += 1
            u = True
            d = False
    else:
        u = d = False

print(cnt)