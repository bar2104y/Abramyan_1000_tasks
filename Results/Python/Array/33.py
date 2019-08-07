from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr(n)
print(a)

l = -1


for i in range(1, n-1):
    if a[i] > a[i-1] and a[i] > a[i+1]:
        l = i
if l == -1:
    print("Не нашел, насяльнике")
else:
    print(i)
