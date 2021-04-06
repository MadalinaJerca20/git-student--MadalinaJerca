def sorter(textbooks):
    return sorted(textbooks, key=str.lower)


print(sorter(['Algebra', 'History', 'Geometry', 'English']), [
    'Algebra', 'English', 'Geometry', 'History'], 'Does not sort strings')
print(sorter(['Algebra', 'history', 'Geometry', 'english']), [
    'Algebra', 'english', 'Geometry', 'history'], 'Does not handle capitalization')
print(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']),
      ['$istory', '**english', 'Alg#bra', 'Geom^try'], 'Does not handle symbols')


'''
# Details
    HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are
    all out of order! Help him sort a list(ArrayList in java) full of textbooks by subject, so he can
    study before the test.
    The sorting should NOT be case sensitive
'''
