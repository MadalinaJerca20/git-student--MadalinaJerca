def evil(n):
    return "It's Odious!" if (bin(n)[2:].count('1') % 2) else "It's Evil!"


print(evil(1), "It's Odious!")
print(evil(2), "It's Odious!")
print(evil(3), "It's Evil!")


'''
# Details
    The number n is Evil if it has an even number of 1's in its binary representation.
    The first few Evil numbers: 3, 5, 6, 9, 10, 12, 15, 17, 18, 20
    The number n is Odious if it has an odd number of 1's in its binary representation.
    The first few Odious numbers: 1, 2, 4, 7, 8, 11, 13, 14, 16, 19
    You have to write a function that determine if a number is Evil of Odious, function should return
    "It's Evil!" in case of evil number and "It's Odious!" in case of odious number.

# Exemplu 1
def evil(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return "It's Odious!" if count & 1 else "It's Evil!"
'''
