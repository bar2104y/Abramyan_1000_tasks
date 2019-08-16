from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

i = 0
while i < len(a):
    a.insert(i,a[i])
    i+=3

print(a)