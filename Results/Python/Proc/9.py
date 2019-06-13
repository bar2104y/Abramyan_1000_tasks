def AddLeftDigit(d,k):
    cnt = 0 #Кол-во цифр в числе
    k1 = k
    while k1 > 0:
        cnt += 1
        k1 //= 10
    k += d*(10**cnt)
    return k

k = 456       #INPUT
da = [3,2,1]  #D1,D2...
for i in da:
    k = AddLeftDigit(i,k)
    print(k)