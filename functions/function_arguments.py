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

# Pitfalls! - Part 1 - Functional - Section 5:76 - In general, be careful when having mutable objects in arguments.
# When a module is loaded, all of the code is run and all of the objects are stored in memory. my_func is created with a keyword argument date=datetime.utcnow(). When the module loads, the date argument will point to the date that the module loaded, not when the function is called (unless the user specifies a new date argument).
from datetime import datetime

# def my_func(date=datetime.utcnow()):
#     print(date)

# Solution
# If the user inputs a date, the date variable assigns itself to that date. If not, date is falsy and will assign date = datetime.utcnow()
# def my_func(date=None):
#     if date is None:
#         date = datetime.utcnow()
#     print(date)

# The opposite of this would be using a mutable object in arguments. We may have wanted to have a=[1,2,3] but somewhere down the module, 4 was appended.
# my_iterable = [1,2,3]
# def my_func(a=my_iterable):
#     print(a)
# my_iterable.append(4)
# my_func()
# Solution - use immutable objects
# my_iterable = (1,2,3)
# def my_func(a=my_iterable):
#     print(a)
# my_iterable.append(4) # Error
# my_func()

# When the module loads, grocery_list is pointing to a memory address of an empty list []. When we call add_item() and assign the return to store1, we are making store1 -> grocery_list in memory. Then when we create a variable, store2, it is pointing to grocery_list again.
# def add_item(item, amt=1, grocery_list=[]):
#     grocery_list.append({f'{item}': amt})
#     return grocery_list
# store1 = add_item('apples', amt=5)
# add_item('bananas', amt=5, grocery_list=store1)
# print(store1)
# store2 = add_item('candy', amt=2)
# add_item('doritos', amt=1, grocery_list=store2)
# print(store2)
# print(store1 is store2)
# Solution - 
# def add_item(item, amt=1, grocery_list=None):
#     if grocery_list is None:
#         grocery_list = []
#     grocery_list.append({f'{item}': amt})
#     return grocery_list
# store1 = add_item('avocados', amt=6)
# add_item('bacon', 1, grocery_list=store1)
# print(store1)
# store2 = add_item('chocolate', amt=1)
# add_item('dog treats', amt=3, grocery_list=store2)
# print(store2)
# print(store1 is store2)