b = [0,1,2,3,4,5,6,7,8,9]
a = [11,12,13,46,78]
#a = [0,1,2,3,4,5,6,7,8,9]
#b = [11,12,13,46,78]


print(a)
print(b)

c = []

if a[len(a)-1] < b[0]:
    c = a+b
else:
    c = b+a
print(c)