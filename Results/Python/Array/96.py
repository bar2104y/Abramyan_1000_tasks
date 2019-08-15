from genarr import genRandomArr
n = int(input("N: "))

a = genRandomArr(n,0,5)
print(a)

i = 0
while i < len(a):
    j = i+1
    while j < len(a):
        if a[j] == a[i]:
            a.pop(j)
        else:
            j += 1
    i+=1
    
print(a)
