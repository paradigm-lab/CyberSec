import random

# Decorators with arguments

# Meta decorator
def power_of(exponent = 2):

    def decorator(func):

        def inner():

            return func() ** exponent

        return inner

    return decorator



@power_of()
def random_odd_digits():

    return random.choice([1, 3, 5, 7, 9])

print(random_odd_digits())


