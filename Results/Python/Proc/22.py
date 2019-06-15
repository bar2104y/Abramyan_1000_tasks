def Calc(a,b,op):#1 -; 2*; 3/ other +
    if op == 1: res = a-b
    elif op == 2: res = a*b
    elif op == 3: res = a/b
    else: res = a+b
    return(res)

a,b = 10, 2
for i in range(4):
    print(Calc(a,b,i)) 