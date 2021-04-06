def is_lock_ness_monster(string):
    substring = ["tree fiddy", "3.50", "three fifty"]
    for txt in substring:
        if txt in string:
            return True
        else:
            return False


print(is_lock_ness_monster(
    "Your girlscout cookies are ready to ship. Your total comes to tree fiddy"))
print(is_lock_ness_monster(
    "I'm from Scottland. I moved here to be with my family. Pls, $3.50 bla bla"))
print(is_lock_ness_monster(
    "Hello, I come from the year 3150 to bring you good news!"))
print(is_lock_ness_monster(
    "By 'tree fiddy' I mean 'three fifty'"))


'''
# Details
    You're on your way to the market when you hear beautiful music coming from a nearby street
    performer. The notes come together like you wouln't believe as the musician puts together patterns
    of tunes. As you wonder what kind of algorithm you could use to shift octaves by 8 pitches or
    something silly like that, it dawns on you that you have been watching the musician for some 10 odd
    minutes. You ask, "How much do people normally tip for something like this?" The artist looks up.
    "Its always gonna be about tree fiddy." It was then that you realize the musician was a 400 foot
    tall beast from the paleolithic era. The Loch Ness Monster almost tricked you! There are only 2
    guaranteed ways to tell if you are speaking to The Loch Ness Monster: A.) It is a 400 foot tall
    beast from the paleolithic era B.) It will ask you for tree fiddy. Since Nessie is a master of
    disguise, the only way accurately tell is to look for the phrase "tree fiddy". Since you are tired
    of being grifted by this monster, the time has come to code a solution for finding The Loch Ness
    Monster. Note: It can also be written as 3.50 or three fifty.

# Exemplu 1
def is_lock_ness_monster(string):
    check = "3.50"
    check2 = "three fifty"
    check3 = "tree fiddy"
    return ((check in string) or (check2 in string) or (check3 in string))

# Exemplu 2
def is_lock_ness_monster(phrase):
    PATTERNS = ('tree fiddy', '3.50', 'three fifty')
    return any(pattern in phrase for pattern in PATTERNS)
'''
