def AddRightDigit(d,k):
    return k*10+d

k = 654 #INPUT
da = [1,2,3] #D1,D2...
for i in da:
    k = AddRightDigit(i,k)
    print(k)