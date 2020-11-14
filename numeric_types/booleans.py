# All objects in Python have a Truthyness or Falsyness. All objects are True except:
    # None
    # False
    # 0
    # Empty sequences (list, tuple, string, etc)
    # Empty mapping types (dictionary, set, etc)
    # Custom classes that implement a __bool__ or __len__ that returns False or 0
# Therefore, every built-in class in Python has a __bool__ or __len__ function

# if 27:
#     print("I'm True!")

# print(bool(None))

# if 0:
#     print("This won't print!")

# my_empty_list = []
# if my_empty_list:
#     print("This won't print!")

# my_truthy_list = [None]
# if my_truthy_list:
#     print("Hello from my_truthy_list!")

# class A:
#     def __bool__(self):
#         return self == 0
# a = A()
# print(bool(a))

# The boolean operators are: not, and, or
# Operator preference (Use parentheses even when not necessary):
    # ()
    # < > <= >= == != in is
    # not
    # and
    # or
# True and False will evaluate first becoming True or False
# print(True or True and False)

# Circuits - booleans are circuits (See Part 1 - Functional - Section 4:55) meaning a closed circuit allows electricity to flow through the circuit (True), and an open circuit cuts the circuit (False). A short-circuit evaluation example would be with the or operator. b doesn't need to be evaluated because a is already True.
# a = -1
# b = False
# if a or b:
#     print('Open circuit!')
# Inversely, a False value on the left side of the equation with the and operator will short-circuit and always evaluate False.
# a = False
# b = True
# if a and b:
#     print('This won\'t print')
# else:
#     print('This short circuited!')

# Imagine we want to populate data to a view function and we want to make sure there is always something to show the user. about_table_field represents an empty field in a database, therefore the about_me variable we use to populate data to the user will have the fallback data of 'n/a'
# about_table_field = ''
# about_me = about_table_field or 'N/A'
# Again used as a fallback to ensure that b is not None
# a = None
# b = a or 1

# or - X or Y: if X is truthy, returns X, otherwise evaluates Y and returns it
# print('a' or [1,2])
# print('' or [1,2])
# x = '' or 'N/A'
# if x:
#     print(x)
# else:
#     print('Error')

# and - X and Y: if X is falsy, return X, otherwise if X is True, evaluate Y and return it
# print(None and 100)
# print(True and 'Evaluating Y')
# We want to avoid a zero division error therefore, we can write an if statement or use the and operator
# a = 2
# b = 0
# if b == 0:
#     print(0)
# else:
#     print(a/b)
# print(b and a/b)
# We want to return the first character from a string if it exists
# s1 = None
# s2 = ''
# s3 = 'Hello World'
# print((s1 and s1[0]) or '')
# print((s2 and s2[0]) or '')
# print((s3 and s3[0]) or '')

# not operator is different than and/or. not is not part of the bool class. and/or both return one of the objects. not returns True/False
print(not True)