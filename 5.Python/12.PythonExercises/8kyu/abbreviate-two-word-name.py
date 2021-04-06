def abbrev_name(name):
    firstLetter = name[0].upper()
    secondIndex = name.find(' ') + 1
    secondLetter = name[secondIndex].upper()
    return firstLetter + "." + secondLetter


print(abbrev_name("Sam Harris"))
print(abbrev_name("Patrick Feenan"))
print(abbrev_name("Evan Cole"))
print(abbrev_name("P Favuzzi"))
print(abbrev_name("David Mendieta"))


'''
# Details
    Write a function to convert a name into initials. This kata strictly takes two words with one space
    in between them. The output should be two capital letters with a dot separating them.
    It should look like this:
        Sam Harris = > S.H

# Exemplu 1
def abbrevName(name):
    return '.'.join(x[0].upper() for x in name.split())

# Exemplu 2
def abbrevName(name):
    x = name
    y = name.split()
    return y[0][0].upper() + "." + y[1][0].upper()
'''
