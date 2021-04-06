def get_drink_by_profession(param):
    drink_by_profession = {
        "Jabroni": "Patron Tequila",
        "School Counselor":	"Anything with Alcohol",
        "Programmer": "Hipster Craft Beer",
        "Bike Gang Member": "Moonshine",
        "Politician": "Your tax dollars",
        "Rapper": "Cristal"
    }
    return drink_by_profession.get(param.title(), "Beer")


def test_basic():
    assert get_drink_by_profession("jabrOni") == "Patron Tequila"
    assert get_drink_by_profession(
        "scHOOl counselor") == "Anything with Alcohol"
    assert get_drink_by_profession("prOgramMer") == "Hipster Craft Beer"
    assert get_drink_by_profession("bike ganG member") == "Moonshine"
    assert get_drink_by_profession("poLiTiCian") == "Your tax dollars"
    assert get_drink_by_profession("rapper") == "Cristal"
    assert get_drink_by_profession("pundit") == "Beer"
    assert get_drink_by_profession("Pug") == "Beer"


'''
# Details
    Write a function getDrinkByProfession/get_drink_by_profession() that receives as input parameter a
    string, and produces outputs according to the following table:
        Input       Output
        "Jabroni"	"Patron Tequila"
        "School Counselor"	"Anything with Alcohol"
        "Programmer"	 "Hipster Craft Beer"
        "Bike Gang Member"	"Moonshine"
        "Politician"	"Your tax dollars"
        "Rapper"	"Cristal"
        *anything else* "Beer"
    Note: anything else is the default case: if the input to the function is not any of the values in the
    table, then the return value should be "Beer."
    Make sure you cover the cases where certain words do not show up with correct capitalization. For
    example, getDrinkByProfession("pOLitiCIaN") should still return "Your tax dollars".

# Exemplu 1
def get_drink_by_profession(param):
    d = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol", "Programmer":"Hipster
    Craft Beer", "Bike Gang Member":"Moonshine", "Politician":"Your tax dollars", "Rapper":"Cristal"}
    if param.title() in d:
        return d[param.title()]
    else:
        return "Beer"

# Exemplu 2
def get_drink_by_profession(param):
    #This function receives an input parameter and produces the corresponding output

    #Step 1 - Produce a dictionary
    Drinks = {'jabroni':'Patron Tequila',
            'school counselor':'Anything with Alcohol',
            'programmer':'Hipster Craft Beer',
            'bike gang member':'Moonshine',
            'politician':'Your tax dollars',
            'rapper':'Cristal'}
    #Step 2 - Turn input to lower case

    profession = param.lower()

    #Step 3 - A for loop that cycles through the keys and has conditional statement

    for key in Drinks:
        if key == profession:
            return Drinks[key]
    return 'Beer'
'''
