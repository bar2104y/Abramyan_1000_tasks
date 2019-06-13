def InvDigits(k):
    c = 0
    tmp = k
    while tmp>0:
        c += 1
        tmp //= 10
    
    for i in range(c-1,0):
        k = ((k // (10 ** i)) * (10 ** c))+(k % (10**i))
    print(k)

for i in range(0,5):
    InvDigits(int(input("Int ")))


        


