from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

i = 1
while i < len(a):
    a.insert(i,a[i])
    a.insert(i,a[i])
    i+=4

print(a)