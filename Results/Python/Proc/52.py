def IsLeapYear(y):
    if y % 4 != 0: return(False)
    if y%100 == 0 and y%400 != 0: return(False)
    return(True)

for i in range(2019):
    print(i, IsLeapYear(i))