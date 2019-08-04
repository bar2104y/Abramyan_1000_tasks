a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n = len(a)
if n % 2:
    for i in range((n-1)//2):
        print(a[i])
        print(a[n-1-i])
    print(a[(n-1)//2])
else:
    for i in range(n//2):
        print(a[i])
        print(a[n-1-i])