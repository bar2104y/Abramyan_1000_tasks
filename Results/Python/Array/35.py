from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr(n)
m = 1000
print(a)


for i in range(1, n-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        m = min(m,a[i])

if m == 1000:
    print("Не нашел, насяльнике")
else:
    print(m)