def bin_to_decimal(inp):
    return int(inp, 2)


print(bin_to_decimal("0"), 0)
print(bin_to_decimal("1"), 1)
print(bin_to_decimal("10"), 2)
print(bin_to_decimal("11"), 3)
print(bin_to_decimal("101010"), 42)
print(bin_to_decimal("1001001"), 73)


'''
# Details
    Complete the function which converts a binary number(given as a string) to a decimal number.

# Exemplu 1
def bin_to_decimal(inp):
    num = 0
    inp = inp[::-1]
    for i in range(len(inp)):
        num += int(inp[i]) * 2 ** i
    return num
'''
