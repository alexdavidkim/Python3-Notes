# All iterables, including strings can be unpacked
# a, b, c, d, e = 'hello'
# print(a, b, c, d, e)

# The Pythonic way to swap variables is below. The reason this works in Python and not languages like Java, is because Python interprets the right hand side and packs it into a tuple (a, b). Then it can unpack those items without having a temporary pointer which is required in Java. (Part 1 - Functional - Section 5:64)
# a, b = 10, 20
# print(a, b)
# b, a = a, b
# print(a, b)

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

# for unpacking UNORDERED types (dictionaries and sets) - Unpacking on the left hand side the way ordered types are unpacked is pointless due to the unordered nature. However, unpacking on the right hand side is useful.