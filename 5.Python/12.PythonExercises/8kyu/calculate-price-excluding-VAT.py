VAT = .15


def excluding_vat_price(price):
    return -1 if price is None else round(price/(1+VAT), 2)


print(excluding_vat_price(230.00), 200.00)
print(excluding_vat_price(123), 106.96)


'''
# Details
    Write a function that calculates the original product price, without VAT.
    If a product price is 200.00 and VAT is 15%, then the final product price (with VAT) is:
        200.00 + 15% = 230.00
    Thus, if your function receives 230.00 as input, it should return 200.00
    Notes:
    VAT is always 15% for the purposes of this Kata.
    Round the result to 2 decimal places.
    If null value given then return -1

# Exemplu 1
def excluding_vat_price(price):
    try:
        return round(price / 1.15, 2)
    except TypeError:
        return -1
'''
