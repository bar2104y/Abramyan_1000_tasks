a = [7,0,1,2,3,4,5,6,8,9]
print(a)

i = 0
while a[i+1] < a[i]:
    a[i], a[i+1] = a[i+1], a[i]
    i += 1

print(a)