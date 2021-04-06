def well(x):
    num_good_ideas = x.count('good')
    return 'Publish!' if num_good_ideas in (1, 2) \
        else 'I smell a series!' if num_good_ideas > 2 else 'Fail!'


print(well(['bad', 'bad', 'bad']))
print(well(['good', 'bad', 'bad', 'bad', 'bad']))
print(well(['good', 'bad', 'bad', 'bad', 'bad', 'good', 'bad', 'bad', 'good']))


'''
# Details
    For every good kata idea there seem to be quite a few bad ones!
    In this kata you need to check the provided array(x) for good ideas 'good' and bad ideas 'bad'. If there
    are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If
    there are no good ideas, as is often the case, return 'Fail!'.

# Exemplu 1
def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"

# Exemplu 2
def well(x):
    if 'good' in x:
        return 'I smell a series!' if x.count('good') > 2 else 'Publish!'
    else:
        return 'Fail!'
'''
