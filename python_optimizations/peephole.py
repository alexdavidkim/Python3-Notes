# Part 1 - Functional - Section 3:27

# Constant expressions
# At compile time, Python will compile the below expression as 1440. The calculation will be viewed as a constant expression thus optimizing against calculating 24 * 60 each time this is presented in the program.
# 24 * 60
# Short sequences of length < 20 will be optimized
# (1, 2) * 5
# 'abc' * 3
# 'hello' + ' world'

# Results differ from version to version (try in Jupyter) due to peephole optimizations being implementation details. How they behave are considered internal details that can and do change from version to version. In fact, the output running this module and directly in Python is very different from Jupyter.
# All of the immutable objects of length < 20 will be compiled as constant expressions. 'the quick brown fox' will be constant but not * 5. 'a' and 'b' will be constants but not the list ['a', 'b'] because lists are mutable.
# def my_func():
#     a = 24 * 60
#     b = (1, 2) * 5
#     c = 'abc' * 3
#     d = 'ab' * 11
#     e = 'the quick brown fox' * 5
#     f = ['a', 'b']
# print(my_func.__code__.co_consts)

# The list is converted to a tuple
# def my_other_func(e):
#     if e in [1,2,3]:
#         pass
# print(my_other_func.__code__.co_consts)

# The set is converted to a frozen set
# def my_other_other_func(e):
#     if e in {1,2,3}:
#         pass
# print(my_other_other_func.__code__.co_consts)

# Sets are much faster than lists or tuples. Watch the video for a performance test.