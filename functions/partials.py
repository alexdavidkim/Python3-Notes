from functools import partial

# my_partial = partial(f, <default values>)

# Partials allow us to not repeat code. We are leveraging the powers function to create square/cube functions that only require the base as an argument as all squares will have an exponent of 2 and all cubes will have an exponent of 3.
# Partials are compiled at run time so be careful when using variables (pointing to the object in memory at runtime) and mutable objects (can be changed).
# def powers(base, exponent):
#     return base ** exponent
# square = partial(powers, exponent=2)
# print(square(4))
# cube = partial(powers, exponent=3)
# print(cube(3))