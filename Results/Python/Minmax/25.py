n = int(input())
last = int(input())

minmult = 10000000

n1,n2 = 0,0

for i in range(n-1):
    tmp = int(input())
    
    if tmp*last < minmult:
        minmult = tmp*last
        n1,n2 = i+1,i+2

    last = tmp

print(n1,n2)