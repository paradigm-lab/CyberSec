"""
Decorator 1: The basics
let's take a look at the basics of python decorators!

What is a decorator?
    A typical decorator is a function that takes a function as an argument, and returns another function. Python has a special syntax to apply decorators to function through a @my_decorator line above the function def.

"""

def turn_into_another_function(func):

    return another_function

@turn_into_another_function
def a_function():
    print ('a_function')

def another_function():
    print("Another function")

a_function()
