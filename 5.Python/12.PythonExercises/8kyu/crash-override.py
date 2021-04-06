FIRST_NAME = {
    'A': 'Alpha',
    'B': 'Beta',
    'C': 'Cache',
    'D': 'Data',
    'E': 'Energy',
    'F': 'Function',
    'G': 'Glitch',
    'H': 'Half-life',
    'I': 'Ice',
    'J': 'Java',
    'K': 'Keystroke',
    'L': 'Logic',
    'M': 'Malware',
    'N': 'Nagware',
    'O': 'OS',
    'P': 'Phishing',
    'Q': 'Quantum',
    'R': 'RAD',
    'S': 'Strike',
    'T': 'Trojan',
    'U': 'Ultraviolet',
    'V': 'Vanilla',
    'W': 'WiFi',
    'X': 'Xerox',
    'Y': 'Y',
    'Z': 'Zero'
}
SURNAME = {
    'A': 'Analogue',
    'B': 'Bomb',
    'C': 'Catalyst',
    'D': 'Discharge',
    'E': 'Electron',
    'F': 'Faraday',
    'G': 'Gig',
    'H': 'Hacker',
    'I': 'IP',
    'J': 'Jabber',
    'K': 'Killer',
    'L': 'Lazer',
    'M': 'Mike',
    'N': 'n00b',
    'O': 'Overclock',
    'P': 'Payload',
    'Q': 'Quark',
    'R': 'Roy',
    'S': 'Spy',
    'T': 'T-Rex',
    'U': 'Unit',
    'V': 'Virus',
    'W': 'Worm',
    'X': 'X',
    'Y': 'Yob',
    'Z': 'Zombie'
}


def alias_gen(f_name, l_name):
    name = FIRST_NAME.get(f_name.title()[0])
    surname = SURNAME.get(l_name.title()[0])
    return f'{name} {surname}' \
        if name and surname \
        else "Your name must start with a letter from A - Z."


basic_tests = (
    (('Mike', 'Millington'), 'Malware Mike'),
    (('Fahima', 'Tash'), 'Function T-Rex'),
    (('Daisy', 'Petrovic'), 'Data Payload'),
    (('Barny', 'White'), 'Beta Worm'),
    (('Hank', 'Kutz'), 'Half-life Killer'),
    (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
    (('walter', 'white'), 'WiFi Worm')
)

for names, result in basic_tests:
    print('{} {}'.format(*names))
    print(alias_gen(*names), result)


'''
# Details
    Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are
    some notable examples from the film Hackers.
    Your task is to create a function that, given a proper first and last name, will return the correct
    alias. Two objects that return a one word name in response to the first letter of the first name and
    one for the first letter of the surname are already given. If the first character of either of the
    names given to the function is not a letter from A - Z, you should return "Your name must start with
    a letter from A - Z."
    Sometimes people might forget to capitalize the first letter of their name so your function should
    accommodate for these grammatical errors.
        FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
        SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}
        alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
        alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'

# Exemplu 1
def alias_gen(f_name, l_name):
    try:
        return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
    except:
        return 'Your name must start with a letter from A - Z.'

# Exemplu 2
def alias_gen(f_name, l_name):
    f = f_name.upper()[0]
    l = l_name.upper()[0]
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if set([f,l]) <= set(abc):
        return FIRST_NAME[f] + " " + SURNAME[l]
    else:
        return "Your name must start with a letter from A - Z."
'''
