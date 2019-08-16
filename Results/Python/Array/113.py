from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

for i in range(n):
    ma = 0
    mai = 0
    for j in range(n-i):
        if a[j] > ma:
            ma = a[j]
            mai = j
    a[n-i-1],a[mai] = a[mai], a[n-1-i]

print(a)
