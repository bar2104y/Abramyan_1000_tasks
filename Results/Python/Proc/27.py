def IsPowerN(k,n):
    while k > n-1:
        k /= n
    if k == 1: return(True)
    else: return(False)
print('x^N = K')
k = int(input('K: '))
n = int(input('N: '))
print(IsPowerN(k,n))