from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

tmp = a[0]

for i in range(1,n-1):
    if a[i] > a[i+1] and a[i] > tmp:
        tmp = a[i]
        a[i] = 0
    else:
        tmp = a[i]
    
print(a)