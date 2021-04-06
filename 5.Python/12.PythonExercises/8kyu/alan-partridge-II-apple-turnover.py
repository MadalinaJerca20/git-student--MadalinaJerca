def apple(x):
    if int(x)**2 > 1000:
        return "It's hotter than the sun!!"
    else:
        return "Help yourself to a honeycomb Yorki for the glovebx."


print(apple('50'))
print(apple(4))
print(apple("12"))
print(apple(60))

'''
# Details
    Alan is known for referring to the temperature of the apple turnover as 'Hotter than the sun!'.
    According to space.com the temperature of the sun's corona is 2,000,000 degrees C, but we will ignore
    the science for now.
    Your job is simple, if (x) squared is more than 1000, return 'It's hotter than the sun!!', else,
    return 'Help yourself to a honeycomb Yorki for the glovebx.'.
    X will be either a number or a string. Both are valid.

# Exemplu 1
def apple(x):
    return 'It\'s hotter than the sun!!' if pow(int(x), 2) > 1000 else 'Help yourself to a honeycomb Yorkie for the glo'
'''
