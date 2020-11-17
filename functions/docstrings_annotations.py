# Docstring - __doc__ in the function class. First line in a function and must be a string. Convention is to use a multi-line string even if only on a single line. Docstrings and annotation have ZERO to do with the actual code (even though it does get compiled at runtime).
# def my_func(a, b=True):
#     """returns a if b is True
#     else returns False
#     """
#     return a if b else False
# print(my_func(10, b=None))
# print(help(my_func))

# Annotation - : <expression> is the format for annotations. I can still make a default value for a parameter after the annotation.
# my_func.__annotations__ are where annotations are stored. Annotations are stored in a dictionary with the parameter being the key and the annotation being the value.
# def my_func(a: 'annotation for a',
#             b: 'annotation for b' = True) -> 'the annotation for return':
#     """"Documentation for my_func()"""
#     print(a, b)
# help(my_func)

# <expression> means that, an expression
# a = 10
# b = 20
# def my_func() -> f'returns a times b: {a*b}':
#     return a*b
# print(my_func.__annotations__)