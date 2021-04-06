import re


def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False
    else:
        uname = re.sub("[a-z0-9_]", "", username)
        if len(uname) == 0:
            return True
        else:
            return False


print(validate_usr('asddsa'),)
print(validate_usr('a'))
print(validate_usr('Hass'))
print(validate_usr('Hasd_12assssssasasasasasaasasasasas'))
print(validate_usr(''))
print(validate_usr('____'))
print(validate_usr('012'))
print(validate_usr('p1pp1'))
print(validate_usr('asd43 34'))
print(validate_usr('asd43_34'))


'''
# Details
    Write a simple regex to validate a username. Allowed characters are:
        lowercase letters,
        numbers,
        underscore
    Length should be between 4 and 16 characters (both included).

# Exemplu 1
def validate_usr(username):
    if len(username) < 4 or len(username) > 16:
        return False
    allowed = 'abcdefghijklmnopqrstuvwxyz0123456789_'
    for i in username:
        if i not in allowed:
            return False
    return True

# Exemplu 2
def validate_usr(username):
    numeric="0123456789"
    if len(username)>=4 and len(username)<=16:
        for letter in username:
            status = 0
            if letter.islower() or letter == "_":
                status = 1
            for num in numeric:
                if letter == num:
                    status = 1
            if status == 0:
                return False
        return True
    else:
        return False

# Exemplu 3
def validate_usr(username):
    import re
    return bool(re.match("^[a-z0-9_]{4,16}$",username))
'''
