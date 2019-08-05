a = [2,8,7,6,5,4,3,2,9]

ml = a[len(a)-1]
mf = a[0]

i = len(a)-1

while i >= 0:
    if a[i] > mf and a[i] < ml:
        print(i)
        exit()
    i -= 1
print(0)