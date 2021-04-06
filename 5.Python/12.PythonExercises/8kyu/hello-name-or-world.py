def hello(name=""):
    return "Hello, World!" if name == "" else "Hello, {}!".format(name.capitalize())


tests = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

for inp, exp in tests:
    print(hello(inp), exp)

print(hello(), "Hello, World!")


'''
# Details
    Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is
    not given (or passed as an empty String).
    Assuming that name is a String and it checks for user typos to return a name with a first capital
    letter (Xxxx).
        Examples:
        hello "john"   => "Hello, John!"
        hello "aliCE"  => "Hello, Alice!"
        hello          => "Hello, World!" # name not given
        hello ''       => "Hello, World!" # name is an empty String

# Exemplu 1
def hello(name=''):
    return f"Hello, {name.title() or 'World'}!"

def hello(name=""):
    return f"Hello, {name.capitalize() if name else 'World'}!"
'''
