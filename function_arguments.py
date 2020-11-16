# *args returns a tuple, **kwargs returns a dictionary
# *args and **kwargs are conventions. What matters is the * and **. You can call args and kwargs anything.

# If an argument is defined with a default value, every argument after it must also have a default value.
# This is not okay.
# def my_func(a, b=100, c):
#     pass

# For if you want to specify optional values for only certain args
# def my_func(a, b=5, c=10):
#     print(f'a: {a}, b: {b}, c: {c}')
# my_func(a=1, c=20)

# Unpacking is taking elements from a list or tuple and assigning them each to variables. See unpacking.py for more. This is almost the same as what is happening when unpacking parameters into arguments with some minor differences.
# When unpacking iterables, Python typically returns a list when using *. However when unpacking *args, Python returns a tuple. Notice how *args gives us the flexibility to have any number of arguments including 0 as long as the first 2 positional arguments are fulfilled.
# def my_func(a, b, *args):
#     print(a)
#     print(b)
#     print(args)
# my_func(10, 20)
# my_func(10, 20, None, True, False, 'hello', [1,2,3])

# To see how to write this with no forced positional argument, the and operator, if statement, see 'Part 1 - Functional - Section 5:69'
# def get_avg(n, *args):
#     count = len(args) + 1
#     total = sum(args) + n
#     return total / count
# print(get_avg(10, 22, 70))

# def func_1(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# my_list = [1,2,3]
# func_1(*my_list)

# Mandatory keyword arguments - *args exhausts all the remaining POSITIONAL arguments therefore, anything after *args can be a forced keyword argument. Try running the below without d=
# def my_func(a, b, *args, d):
#     print(args)
#     print(d)
# my_func(10, 20, 'a', None, True, d='required!')

# Forcing NO positional arguments - * indicates no positional arguments after this point, only keyword arguments. Try running below without d=.
# def my_func(*, d):
#     print(d)
# my_func(d=100)

# def another_func(a, b=1, *, d, e=True):
#     print(a)
#     print(b)
#     print(d)
#     print(e)
# another_func('a', d='required!')

# **kwargs - returns a dictionary
# def my_func(*, d, **kwargs):
#     print(d)
#     print(kwargs)
# my_func(d=None, a=100, b=200, c=True)
# my_func(d='No kwargs, just an empty dictionary!')

# def my_func(**kwargs):
#     print(kwargs)
# my_func(a=1, b=2, c=3)

# def args_and_kwargs_func(*args, **kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     print(kwargs)
# args_and_kwargs_func(10, 20, True, False, a=1000, b=2000, c=5000)