def year_days(year):
    return "{} has {} days".format(year,
                                   366 if (year % 4 == 0 and year % 100 != 0)
                                   or (year % 400 == 0) else 365)


print(year_days(0), '0 has 366 days')
print(year_days(-64), '-64 has 366 days')
print(year_days(2016), '2016 has 366 days')
print(year_days(1974), '1974 has 365 days')
print(year_days(-10), '-10 has 365 days')
print(year_days(666), '666 has 365 days')
print(year_days(1857), '1857 has 365 days')
print(year_days(2000), '2000 has 366 days')
print(year_days(-300), '-300 has 365 days')
print(year_days(-1), '-1 has 365 days')


'''
# Details
    A variation of determining leap years, assuming only integers are used and years can be negative
    and positive.
    Write a function which will return the days in the year and the year entered in a string. For example
    2000, entered as an integer, will return as a string 2000 has 366 days
    There are a few assumptions we will accept the year 0, even though there is no year 0 in the Gregorian
    Calendar. Also the basic rule for validating a leap year are as follows
    Most years that can be divided evenly by 4 are leap years.
    Exception: Century years are NOT leap years UNLESS they can be evenly divided by 400.
    So the years 0, -64 and 2016 will return 366 days. Whilst 1974, -10 and 666 will return 365 days.

# Exemplu 1
def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)

import calendar

# Exemplu 2
def year_days(year):
    if calendar.isleap(year):
        return '{0} has 366 days'.format(year)
    else:
        return '{0} has 365 days'.format(year)

# Exemplu 3
from calendar import isleap

def year_days(year):
    return f"{year} has {365 + isleap(year)} days"
'''
