def name_shuffler(str_):
    first, second = str_.split()
    return " ".join([second, first])


print(name_shuffler('john McClane'))
print(name_shuffler('Mary jeggins'))
print(name_shuffler('tom jerry'))


'''
# Details
    Write a function that returns a string in which firstname is swapped with last name.
        name_shuffler('john McClane'); => "McClane john"

# Exemplu 1
def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])

# Exemplu 2
def name_shuffler(str_):
    words = str_.split()
    words = list(reversed(words))
    return " ".join(words)
'''
