# If an argument is defined with a default value, every argument after it must also have a default value.
# This is not okay.
# def my_func(a, b=100, c):
#     pass

# For if you want to specify optional values for only certain args
# def my_func(a, b=5, c=10):
#     print(f'a: {a}, b: {b}, c: {c}')
# my_func(a=1, c=20)

# Unpacking is taking elements from a list or tuple and assigning them each to variables. This is exactly what is happening when passing arguments to a function
a, b, c = [1,2,3]
print(a, b, c)