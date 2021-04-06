def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


print(divisible_by([1, 2, 3, 4, 5, 6], 2), [2, 4, 6])
print(divisible_by([1, 2, 3, 4, 5, 6], 3), [3, 6])
print(divisible_by([0, 1, 2, 3, 4, 5, 6], 4), [0, 4])
print(divisible_by([0], 4), [0])
print(divisible_by([1, 3, 5], 2), [])


'''
# Details
    Complete the function which takes two arguments and returns all numbers which are divisible by the
    given divisor. First argument is an array of numbers and the second is the divisor.
        Example
        divisible_by([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]

# Exemplu 1
def divisible_by(numbers, divisor):
    div_by = []
    for num in numbers:
        if num % divisor == 0:
            div_by.append(num)
    return div_by
'''
