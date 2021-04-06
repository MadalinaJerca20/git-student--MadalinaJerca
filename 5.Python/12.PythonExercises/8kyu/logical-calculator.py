def logical_calc(array, op):
    if op == "XOR":
        op = "^"
    s = op.lower().join([" " + str(i) + " " for i in array]).strip()
    return eval(s)


print(logical_calc([True, False], "AND"))
print(logical_calc([True, False], "OR"))
print(logical_calc([True, False], "XOR"))
print(logical_calc([True, True, False], "AND"))
print(logical_calc([True, True, False], "OR"))
print(logical_calc([True, True, False], "XOR"))


'''
# Details
    Your task is to calculate logical value of boolean array. Test arrays are one-dimensional and their
    size is in the range 1-50.
    Links referring to logical operations: AND, OR and XOR.
    You should begin at the first value, and repeatedly apply the logical operation across the remaining
    elements in the array sequentially.
    First Example:
        Input: true, true, false, operator: AND
        Steps: true AND true -> true, true AND false -> false
        Output: false
    Second Example:
        Input: true, true, false, operator: OR
        Steps: true OR true -> true, true OR false -> true
        Output: true
    Third Example:
        Input: true, true, false, operator: XOR
        Steps: true XOR true -> false, false XOR false -> false
        Output: false
            Input:
            boolean array, string with operator' s name: 'AND', 'OR', 'XOR'.
            Output:
            calculated boolean

# Exemplu 1
def logical_calc(array, op):
    return reduce(eval('bool.__'+op.lower()+'__'),array)

# Exemplu 2
def logical_calc(array, op):
    res = array[0]
    for x in array[1:]:
        if op == "AND":
            res &= x
        elif op == "OR":
            res |= x
        else:
            res ^= x
    return res #boolean

# Exemplu 3
from operator import xor

def logical_calc(array, op):
    m = {
        "AND": all(array),
        "OR": any(array),
        "XOR": reduce(lambda i, j: int(i) ^ int(j), array)
    }
    return m[op]

# Exemplu 4
from functools import reduce


def logical_calc(array, op):
    return reduce(lambda x,y: {'OR': x or y, 'AND': x and y, 'XOR': x ^ y}[op], array)
'''
