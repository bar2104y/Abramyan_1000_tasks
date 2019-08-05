a = [9,8,7,6,5,4,3,2,5]

m = a[len(a)-1]

for i in a:
    if i < m:
        print(i)
        exit()
print(0)
