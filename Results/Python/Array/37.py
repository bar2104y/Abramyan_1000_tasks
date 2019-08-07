from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr (n)
print(a)

cnt = 0
f = False

for i in range(1,n):
    if a[i] > a[i-1]:
        if not f:
            cnt += 1
            f= True
    else:
        f = False

print(cnt)