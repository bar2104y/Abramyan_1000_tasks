def IsPower5(k):
    while k>4:
        k /= 5
    if k == 1: return(True)
    else: return(False)

print(IsPower5(int(input('K: ')))) 
    