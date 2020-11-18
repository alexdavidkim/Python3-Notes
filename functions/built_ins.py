# I wrote the range function this way to prove a point. range(x) is not calculated until run time. So if you print(result), the output is range(0, 100). Only when it is called is it calculated. range() differs from map, filter, reduce in that you can re-use it (see IMPORTANT note in map, filter, reduce section)
# result = range(10)
# print(result)
# for x in result:
#     print(x)
# for x in result:
#     print(x)

# str = 'hello'
# for i, x in enumerate(str):
#     print(i, x)

# num = 10
# print(isinstance(num, int))

# Illustrating that variables are simply pointers or references to objects in memory. Those objects store the type of the object (str, int, etc). This is called a dynamic typing language. Other languages like Java and C++ require the variable to be assigned to a data type and can not alter from that type. Also, when you change the value associated with a variable, you are not changing the current object in memory, you are creating a new object in a new location in memory.
# my_var = 'hello'
# print(type(my_var))
# print(id(my_var))
# my_var = 10
# print(type(my_var))
# print(id(my_var))

# SEE BELOW FOR LIST COMPREHENSIONS VERSIONS OF THE FOLLOWING CODE
# map(f, *iterables) - map() takes a function and applies the return statement equally to the elements in all iterables. However, if iterable1 is 3 elements and iterable 2 is 4 elements, map() will only apply to the first 3 elements.
# square_me = [2,3,4]
# print(list(map(lambda x: x**2, square_me)))
# add_me_to_below = [1,2,3,4,5]
# add_me_to_above = [11,12,13,14,15]
# print(list(map(lambda x, y: x + y, add_me_to_below, add_me_to_above)))

# filter(f, iterable) - filter() filters a single iterable based on the given function return. None can be passed as the function which will remove all Falsy values from the iterable.
# my_list = [0,1,2,3,4, None, False]
# print(list(filter(None, my_list)))
# get_the_evens = [0,1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x: x % 2 == 0, get_the_evens)))

# zip(*iterables) - Think of a zipper, you take more than one iterable and join them to return an iterator with the elements sharing indexes combined as a tuple. Will end at the shortest iterable.
# list_1 = [True, False, None]
# list_2 = [10, 20, 30, 40]
# tuple_1 = ('a', 'b', 'c', 'd')
# print(list(zip(list_1, list_2, tuple_1)))

# Zip example use case - We want to enumerate an unknown amount of items in an iterable. 
# iter_1 = range(100)
# iter_2 = 'abcd'
# print(list(zip(iter_1, iter_2)))

# List comprehensions - [<expression1> for <varname(s)> in <iterable> if <expression2>]

# square_me example above
# square_me = [2,3,4]
# print([x**2 for x in square_me])

# Combining map() and zip()
# list_1 = [1,2,3]
# list_2 = [10,20,30]
# print([x+y for x,y in zip(list_1, list_2)])

# filter()
# get_the_evens = [0,1,2,3,4,5,6,7,8,9,10]
# print([x for x in get_the_evens if x % 2 == 0])

# map() and filter()
# iter_1 = range(10)
# print([x**2 for x in iter_1 if x**2 < 25])

# IMPORTANT - Below applies for map(), filter(), zip()
# TODO - See Part 1 - Functional - Section 6:89 - He talks about generators. What is happening below is this: my_list_squared is a map object. That means that the actual results in the list are not calculated yet. They are calculated at run time to save on calculations. If we called the for loop to only run for the first 3 elements, it would only calculate those 3 elements and not the remaining. Another consequence of this is that when my_list_squared is assigned to the map object, it won't show errors until run time. 
# I am still not sure why the map object is essentially thrown away and I think it has to do with generators which is something I haven't learned yet. The solution is to simply wrap the map object in a list and it will be calculated when assigned to my_list_squared.
# my_list = [1,2,3,4,5]
# my_list_squared = map(lambda x: x**2, my_list)
# print(my_list_squared)
# for x in my_list_squared:
#     print(x)
# for x in my_list_squared:
#     print(x)