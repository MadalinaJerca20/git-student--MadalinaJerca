def duck_duck_goose(players, goose):
    return players[(goose - 1) % (len(players))].name


print(duck_duck_goose(players, 1),  "a")
print(duck_duck_goose(players, 3),  "c")
print(duck_duck_goose(players, 10), "z")
print(duck_duck_goose(players, 20), "z")
print(duck_duck_goose(players, 30), "z")


'''
# Details
    The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one
    is chosen.
    Task: Given an array of Player objects (an array of associative arrays in PHP) and an index (1-based),
    return the name of the chosen Player(name is a property of Player objects, e.g Player.name)
        Example:
        duck_duck_goose([a, b, c, d], 1) should return a.name
        duck_duck_goose([a, b, c, d], 5) should return a.name
        duck_duck_goose([a, b, c, d], 4) should return d.name

# Exemplu 1
def duck_duck_goose(players, goose):
    i = 0
    count = 0
    while count <= goose:
        if count == (goose - 1):
            return players[i].name
        else:
            count += 1
            i = (i + 1) % len(players)
'''
