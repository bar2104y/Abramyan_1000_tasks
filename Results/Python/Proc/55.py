def IsLeapYear(y):
    if y % 4 != 0: return(False)
    if y%100 == 0 and y%400 != 0: return(False)
    return(True)

def MonthDays(m,y):
    if m == 2:
        return(29 if IsLeapYear(y) else 28 )
    else:
        return (31 if (m%7)%2 != 0 or m == 7 else 30)

def NextDate(d,m,y):
    if d == MonthDays(m,y):
        d = 1
        if m == 12:
            m = 1
            y += 1
        else: m+=1
    else: d += 1
    return(d,m,y)

print(NextDate(31,12,2015))
