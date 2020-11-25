# All iterables, including strings can be unpacked
# a, b, c, d, e = 'hello'
# print(a, b, c, d, e)

# The Pythonic way to swap variables is below. The reason this works in Python and not languages like Java, is because Python interprets the right hand side and packs it into a tuple (a, b). Then it can unpack those items without having a temporary pointer which is required in Java. (Part 1 - Functional - Section 5:64)
# a, b = 10, 20
# print(a, b)
# b, a = a, b
# print(a, b)

# Unpacking *args and **kwargs - custom_print takes in a function, print. *args represent the objects that are passed into the standard print function. **kwargs are optional parameters where sep=' ' and end='\n' are defaults. 
# def custom_print(f, *args, **kwargs):
#     f(*args, **kwargs)
# custom_print(print, 'i', 'love', 'life', sep='-', end=' :) :) :)\n')

# The exception to unpacking this way are dictionaries and sets because they are unordered and therefore you can not rely on them to unpack in the order which you specify.
# my_dict = {
#     'key1': 1,
#     'key2': 2,
#     'key3': 3,
# }
# my_set = {'p', 'y', 't', 'h', 'o', 'n'}
# a, b, c = my_dict
# print(a, b, c)
# a, b, c, d, e, f = my_set
# print(a, b, c, d, e, f)

# * for unpacking ORDERED types (not dictionaries and sets)
# my_list = [1,2,3,4,5,6,7]
# a, *b = my_list
# print(a, b)
# Regardless of the iterable type, the remaining variables will be put into a list
# my_tuple = (1,2,3,4,5,6,7)
# c, *d = my_tuple
# print(c, d)
# my_str = 'hello world'
# e, f, *g = my_str
# print(e, f, g)
# Variations of below also work
# my_list = [1,2,3,4,5,6,7]
# a, b, *c, d = my_list
# print(a, b, c, d)
# Unpacking on the right hand side of an expression
# my_list_1 = [None, {'1': 1, '2': 2}, 3.14, 'hello']
# my_list_2 = [True, False, None, 'world']
# my_new_tuple = *my_list_1, *my_list_2
# print(type(my_new_tuple))
# print(my_new_tuple)

# for unpacking UNORDERED types (dictionaries and sets) - Unpacking on the left hand side the way ordered types are unpacked is pointless due to the unordered nature. However, unpacking on the right hand side is useful. (Order still not guaranteed)
# my_dict_1 = {'one': 1, 'two': 2}
# my_dict_2 = {'three': 3, 'four': 4}
# my_dict_3 = {'four': 4, 'five': 4}
# new_unpacked_list = [*my_dict_1, *my_dict_2, *my_dict_3]
# new_unpacked_set = {*my_dict_1, *my_dict_2, *my_dict_3}
# print(new_unpacked_list)
# print(new_unpacked_set)

# Nested unpacking - can perform with any iterable
# a, b, (c, d) = [1, 2, [3, 4]]
# print(a)
# print(b)
# print(c)
# print(d)

# Dummy variables - when we don't care about a particular variable (it still counts as a variable but we are indicating we don't need it)
# city, _, population = ('Beijing', 'China', 21_000_000)

# Dummy variables (more than one)
# record = ('DJIA', 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.71)
# Instead of this
# symbol, year, month, day, open, high, low, close = record 
# Do this
# symbol, year, month, day, *_, close  = record
# print(*_)