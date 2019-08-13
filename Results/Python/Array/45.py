from genarr import genRandomArr
#Самое простое решение O = n^2
n = int(input("N: "))

a = genRandomArr(n)
print(a)

mind = 10002
b = [0,0]

for i in range(n):
    for j in range(i+1,n):
        if abs(a[i]-a[j]) < mind:
            mind = abs(a[i]-a[j])
            b = [i,j]

print(b)