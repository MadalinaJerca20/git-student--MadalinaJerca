def century(year):
    return (year + 99)//100


print(century(1705), 18, 'Testing for year 1705')
print(century(1900), 19, 'Testing for year 1900')
print(century(1601), 17, 'Testing for year 1601')
print(century(2000), 20, 'Testing for year 2000')
print(century(356), 4, 'Testing for year 356')
print(century(89), 1, 'Testing for year 89')


'''
# Details
    The first century spans from the year 1 up to and including the year 100, The second - from the
    year 101 up to and including the year 200, etc.
    Given a year, return the century it is in.
        Input , Output Examples ::
        centuryFromYear(1705)  returns (18)
        centuryFromYear(1900)  returns (19)
        centuryFromYear(1601)  returns (17)
        centuryFromYear(2000)  returns (20)

# Exemplu 1
def century(year):
    if year%100==0:
        return year//100
    else:
        return year//100+1
'''
