def build_string(*args):
    return 'I like {}!'.format(", ".join(args))


print(build_string('Cheese', 'Milk', 'Chocolate'))
print(build_string('Cheese', 'Milk'))
print(build_string('Chocolate'))


'''
# Details
    Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template
    feature, Help Timmy with his string template so it works as he expects!

# Exemplu 1
def build_string(*args):
    return "I like %s!" % ", ".join(args)
'''
