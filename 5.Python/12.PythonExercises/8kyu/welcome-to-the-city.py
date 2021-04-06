def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"


print(say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
print(say_hello(['Franklin', 'Delano', 'Roosevelt'], 'Chicago', 'Illinois')
print(say_hello(['Wallace', 'Russel', 'Osbourne'], 'Albany', 'New York')


'''
# Details
    Create a method sayHello/say_hello/SayHello that takes as input a name, city, and state to welcome a
    person. Note that name will be an array consisting of one or more values that should be joined
    together with one space between each, and the length of the name array in test cases will vary.
        Example:
        say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
    This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

# Exemplu 1
def say_hello(name, city, state):
  return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)

# Exemplu 2
def say_hello(name, city, state):
    return 'Hello, %s! Welcome to %s, %s!' % (' '.join(name), city, state)

# Exemplu 3
def say_hello(name, city, state):
    name = " ".join(name)
    return "Hello, %s! Welcome to %s, %s!" %(name,city,state)
'''
