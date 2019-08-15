from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

i = len(a)-1
while i >= 0:
    j = i-1
    while j >= 0:
        if a[j] == a[i]:
            a.pop(j)
            i -= 1
        j -= 1
        
    i-=1
    
print(a)
