from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

i = 0
while i < len(a):
    if a[i] % 2 == 1:
        a.pop(i)
    else:
        i += 1
    
print(a)
