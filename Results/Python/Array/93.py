from genarr import genLinearArr
n = int(input("N: "))

a = genLinearArr(n)
print(a)

i = 0
while i < len(a):
    a.pop(i)
    i += 1
    
print(a)
