from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,1)
print(a)

i = 0
while i < len(a)-1:
    if a[i] == a[i+1]:
        a.pop(i+1)
    else:
        i+=1
    
print(a)
