a = [4,9,8,7,6,5,3,2,1,0]
print(a)
i = 0
while i < len(a)-1:
    if a[i+1] > a[i]:
        a[i], a[i+1] = a[i+1], a[i]
    i += 1
print(a)