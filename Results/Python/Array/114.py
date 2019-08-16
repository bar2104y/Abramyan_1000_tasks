from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

for i in range(1,n):
    k = a[i]
    j = i-1
    while j >= 0 and a[j] > k:
        a[j+1] = a[j]
        j -= 1
    
    a[j+1] = k

print(a)
