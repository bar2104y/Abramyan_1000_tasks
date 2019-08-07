from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr(n)
print(a)

cnt = 0

for i in range(1, n):
    if a[i] > a[i-1]:
        cnt += 1
        print(i)

print("Cnt:", cnt)