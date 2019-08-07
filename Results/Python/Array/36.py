from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr(n)
m = -1
print(a)


for i in range(1, n-1):
    if not (a[i] > a[i-1] and a[i] > a[i+1]) and not (a[i] < a[i-1] and a[i] < a[i+1]):
        m = max(m, a[i])




print(max(m, a[0], a[n-1]))