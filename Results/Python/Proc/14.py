def SHiftRight3(a,b,c):
#    tmp = a
#    a = c
#    c = b
#    b = tmp
#    return(a,b,c)
    return(c,a,b)

a = [[1,2,3],
    [2,4,6],
    [9,8,7]]
for i in a:
    print(SHiftRight3(i[0],i[1],i[2]))