def IsPrime(n):
    for i in range(2,int(n/2)+1):
        print(i)
        if n % i == 0: return(False)
    
    return(True)

print(IsPrime(int(input('N: '))))