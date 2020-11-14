# Tuples are immutable. The "exception" to this is when a mutable object, such as a list, is an element of the tuple. In this case, we could change the contents of the list and it would appear changed in the tuple (even though the memory address for the list stays the same).
# my_list = [1,2,3]
# my_tuple = (1, None, my_list)
# my_list = [1,2,3,4]
# print(my_list)
# print(my_tuple)

# The () to create a tuple are not required but suggested. What really designates a tuple is a comma. The only exception is when you want to create an empty tuple.
# a = 1,2,3
# print(type(a))
# b = ()
# print(type(b))
# c = (1)
# print(type(c))
# d = (1,)
# print(type(d))