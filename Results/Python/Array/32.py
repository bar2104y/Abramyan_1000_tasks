from genarr import genRandomArr
n = int(input("N: "))
a = genRandomArr(n)
print(a)


for i in range(1, n-1):
    if a[i] < a[i-1] and a[i] < a[i+1]:
        print(i)
        exit()

print("Не нашел, насяльнике")