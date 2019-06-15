def DigitN(k,n):
    for i in range(n):
        d = k % 10
        k //= 10
    return(d)

k = int(input('K: '))
n = int(input('N: '))
print(DigitN(k,n))