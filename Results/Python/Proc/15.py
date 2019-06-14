def SHiftRight3(a,b,c):
#    tmp = c
#    c = a
#    a = b
#    b = tmp
#    return(a,b,c)
    return(b,c,a)

a = [[1,2,3],
    [2,4,6],
    [9,8,7]]
for i in a:
    print(SHiftRight3(i[0],i[1],i[2]))