def even_or_odd(number):
    return 'Even' if number % 2 == 0 else 'Odd'


print(even_or_odd(2), "Even")
print(even_or_odd(0), "Even")
print(even_or_odd(7), "Odd")
print(even_or_odd(1), "Odd")
print(even_or_odd(-1), "Odd")


'''
# Details
    Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even"
    for even numbers or "Odd" for odd numbers.

# Exemplu 1
def even_or_odd(number):
  return ["Even", "Odd"][number % 2]
'''
