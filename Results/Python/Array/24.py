n = int(input())
a=[]

for i in range(n):
    a.append(i)

d = a[1] - a[0]

for i in range(1,n-1):
    if a[i+1]-a[i] != d:
        exit("0")

print("Yes")