from functools import wraps

# A typical decorator With an inner() function


# Mapper is going to take a camelcase function and change into a map
def mapper(func):

    @wraps(func)
    def inner(list_of_values):

        """ This is the inner() function """
        return [func(value) for value in list_of_values]

    return  inner




@mapper
def camelcase(s):
    
    """
        Turn Strings_like_this into StringsLikeThis
        List Comprehension
    """

    return ''.join([word.capitalize() for word in s.split('_')])

names = [
    'Rick_ross',
    'a$ap_rocky',
    'snoop_dogg'
]

print(camelcase(names))
print(camelcase.__doc__)
