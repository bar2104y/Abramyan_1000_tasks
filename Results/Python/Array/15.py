a = [0,1,2,3,4,5,6,7]

i,k = 1,2
while i < len(a):
    print(a[i])
    i += k

i,k = len(a)-2+len(a)%2, 2
while i >= 0:
    print(a[i])
    i -= k