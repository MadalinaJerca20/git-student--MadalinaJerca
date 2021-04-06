def count_sheeps(sheep):
    return sheep.count(True)


array1 = [True,  True,  True,  False,
          True,  True,  True,  True,
          True,  False, True,  False,
          True,  False, False, True,
          True,  True,  True,  True,
          False, False, True,  True]

print(count_sheeps(array1), 17, "There are 17 sheeps in total, not %s" % count_sheeps(array1))


'''
# Details
  Consider an array/list of sheep where some sheep may be missing from their place. We need a function
  that counts the number of sheep present in the array (true means present).
    For example,
    [True,  True,  True,  False,
      True,  True,  True,  True ,
      True,  False, True,  False,
      True,  False, False, True ,
      True,  True,  True,  True ,
      False, False, True,  True]
    The correct answer would be 17.
  Hint: Don't forget to check for bad values like null/undefined

# Exemplu 1
def count_sheeps(sheep):
  return len([x for x in sheep if x])

# Exemplu 2
def count_sheeps(arrayOfSheeps):
    sheep_present = 0
    for sheep in arrayOfSheeps:
        if sheep:
            sheep_present += 1
    return sheep_present
'''
