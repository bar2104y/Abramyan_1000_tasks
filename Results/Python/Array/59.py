from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

b = [0]
sum = 0

for i in range(1,n):
    sum += a[i]
    b.append(sum/i)

print(b)