def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None


ts = (
    ("1.0", 1.0),
    ("a", None),
    ("234.0234", 234.0234)
)

for t in ts:
    print(parse_float(t[0]), t[1])


'''
# Details
    Write function parse_float which takes a string/list and returns a number or 'none' if conversion
    is not possible.
'''
