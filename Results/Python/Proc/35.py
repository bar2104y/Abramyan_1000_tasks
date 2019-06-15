def Fact2(n):
    i = 2 if n % 2==0 else 1
    res = 1
    while i <= n:
        res*=i
        i += 2
    return(res)

print(Fact2(6))