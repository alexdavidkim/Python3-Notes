# Part 1 - Functional - Section 3:20
# Immutable objects are objects stored in memory that can never have their internal state modified. If we have my_var = 'hello', my_var is pointing to an object in memory that is storing the value 'hello' as a string data type. If we re-assign my_var to another string, we are not changing the object in memory, we are creating an entirely new object in memory with a data type and content.
# Immutable:
    # Numbers (int, float, Booleans, etc)
    # Strings
    # Tuples
    # Frozen sets
    # User-defined classes
# Mutable:
    # Lists
    # Sets
    # Dictionaries
    # User-defined classes

# Tuples are immutable in that we can not add, remove, or modify the elements inside them. HOWEVER, the objects in my_tuple below are lists, which ARE mutable. Therefore, they can be changed.
# list_a = [1, 2]
# list_b = [3, 4]
# my_tuple = (list_a, list_b) 
# print(my_tuple)
# print(id(my_tuple))
# list_a.append(3)
# list_b.append(5)
# print(my_tuple)
# print(id(my_tuple))
# This tuple however is completely immutable because the elements are all integers which are immutable.
# another_tuple = (1,1,1)
# for x in another_tuple:
#     print(id(x))

# Lists are mutable so I can change the state of my_list with append. However, with my_other_list and last_list, I am changing the object in memory.
# my_list = [1, 2, 3]
# print(id(my_list))
# my_list.append(4)
# print(id(my_list))
# my_other_list = [1, 2, 3]
# print(id(my_other_list))
# my_other_list = [1, 2, 3, 4]
# print(id(my_other_list))
# last_list = [1, 2, 3]
# print(id(last_list))
# last_list = last_list + [4]
# print(id(last_list))

# Dictionaries are mutable and we can preserve the object in memory by using the syntax my_dict['key'] = value
# my_dict = {
#     'key-one': 1,
#     'key-two': None
# }
# print(id(my_dict))
# my_dict['key-three'] = [1,2,3]
# print(id(my_dict))

# Part 1 - Functional - Section 3 - Function Arguments and Mutability
# When you are using arguments in functions, you are providing the function a reference to the object that the variable points to
# Immutable objects such as strings are safe from unintended side effects. my_var is not being modified when passed to my_func()
# def my_func(str_obj):
#     str_obj = str_obj + ' world'
#     return str_obj
# my_var = 'hello'
# print(my_var)
# print(my_func(my_var))
# print(my_var)
# Mutable objects can suffer from unintended side effects such as changing the state of the variable.
# def my_other_func(mut_obj):
#     mut_obj.append(100)
# my_list = [1,2,3]
# print(my_list)
# my_other_func(my_list)
# print(my_list)

