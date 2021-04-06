from math import floor


def litres(time):
    return floor(0.5 * time)


print(litres(2), 1, 'should return 1 litre')
print(litres(1.4), 0, 'should return 0 litres')
print(litres(12.3), 6, 'should return 6 litres')
print(litres(0.82), 0, 'should return 0 litres')
print(litres(0), 0, 'should return 0 litres')


'''
# Details
    Nathan loves cycling.
    Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of
    cycling. You get given the time in hours and you need to return the number of litres Nathan will
    drink, rounded to the smallest value.
        For example:
        time = 3 ----> litres = 1
        time = 6.7---> litres = 3
        time = 11.8--> litres = 5

# Exemplu 1
def litres(time):
    return time // 2

# Exemplu 2
def litres(time):
    return int(time/2)
'''
