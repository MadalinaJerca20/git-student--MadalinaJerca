def mouth_size(animal):
    return 'small' if animal.lower() == 'alligator' else 'wide'


print(mouth_size("toucan"), "wide")
print(mouth_size("ant bear"), "wide")
print(mouth_size("alligator"), "small")


'''
# Details
    The wide mouth frog is particularly interested in the eating habits of other creatures.
    He just can't stop asking the creatures he encounters what they like to eat. But then he meet the
    alligator who just LOVES to eat wide-mouthed frogs! When he meets the alligator, it then makes a tiny
    mouth. Your goal in this kata is to create complete the mouth_size method this method take one
    argument animal which corresponds to the animal encountered by frog. If this one is an alligator
    (case insensitive) return small otherwise return wide.
        ("toucan") -> "wide")
        ("ant bear") -> "wide")
        ("alligator") -> "small")

# Exemplu 1
def mouth_size(animal):
  return 'wide' if animal.lower() != 'alligator' else 'small'

# Exemplu 2
def mouth_size(animal):
    mouth = {'alligator':'small'}
    return mouth.get(animal.lower(), 'wide')
'''
