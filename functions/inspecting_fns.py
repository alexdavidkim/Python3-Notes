# Part 1 - Functional - Section 6:85-86

import inspect

# TODO: Python will track to-do's which can be accessed with inspect.getcomments()
# This is a comment in the example function
def my_func(a: int,  
            b: int = 1, 
            *args: 'additional positional args',
            kw1: 'first keyword only arg',
            kw2: 'second keyword only arg' = None,
            **kwargs: 'additional keyword-only args') -> 'return annotation goes here':
    """This is the docstring for the example function"""
    local_var_1 = None
    local_var_2 = None
    pass

# dir(obj) - takes an object and returns a list of valid attributes
# my_func.my_custom_attribute = 'foobar'
# print(dir(my_func))

# returns the name of the function - sometimes we don't know the name of a function that is being passed
# print(my_func.__name__)
# def call_func(f):
#     print(f is my_func)
#     print(f.__name__)
# call_func(my_func)

# returns a tuple with positional argument defaults
# print(my_func.__defaults__)

# returns a dictionary with keyword argument defaults
# print(my_func.__kwdefaults__)

# obj.__code__ returns a code object with several features
# print(my_func.__code__)
# print(dir(my_func.__code__))

# returns a tuple with variable names (parameters and local scope)
print(my_func.__code__.co_varnames)

# returns a bool if object is a function
# print(inspect.isfunction(my_func))

# returns a bool if object is a method
# print(inspect.ismethod(my_func))

# returns a bool if object is either a function or method
# print(inspect.isroutine(my_func))

# returns a string containing the entire object (including docstrings and annotations)
# print(inspect.getsource(my_func))

# returns the module of the object
# print(inspect.getmodule(my_func))
# print(inspect.getmodule(print))

# returns comments and use for to-do's
# print(inspect.getcomments(my_func))

# returns docstring
# print(my_func.__doc__)

# returns annotations
# print(my_func.__annotations__)
