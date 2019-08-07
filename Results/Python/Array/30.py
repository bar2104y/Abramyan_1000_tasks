from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr(n)
print(a)

cnt = 0

for i in range(n-1):
    if a[i] > a[i+1]:
        cnt += 1
        print(i)

print(cnt)