from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n)
print(a)

tmp = a[0]
a[0] = float('{:.2f}'.format((a[0]+a[1])/2))

for i in range(1,n-1):
    tmp = a[i]
    a[i] = float('{:.2f}'.format((tmp+a[i]+a[i+1])/3))

a[n-1] = float('{:.2f}'.format((a[n-1]+tmp)/2))
    
print(a)