# A decorator function takes in a function argument, decorates it with added functionality, and returns that same function with its new features (a closure). 

    # General blueprint - 

    # def decorator(original_function):
        # free vars
        # def decorated_function(*args, **kwargs):
            # does something
            # return original_function(*args, **kwargs)
        # return decorated_function
    # original_function = decorator(original_function)

    # ... is the same as writing

    # @decorator
    # def original_function():
        # code

# add(x,y) gets passed to counter(fn) as the function. inner(*args) passes in x,y from add(). count is part of the closure. The purpose of this closure is to print how many times a function has been called (print line). inner returns add(x, y) executed. counter(fn) returns this return from inner. 
def counter(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'Function {fn.__name__} was called {count} times.')
        return fn(*args, **kwargs)
    return inner

@counter
def add(x, y):
    return x + y

fn1 = add
fn2 = add
print(fn1(1,2))
print(fn1(1,3))
print(fn2(10, 20))
print(fn2(10, 30))






from functools import wraps
# functools.wraps puts the original function's metadata (docstrings, annotations, parameters, etc.) when called as opposed to inner

# def counter(f):
#     count = 0
#     @wraps(f)
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'Running {f.__name__}... {count} times')
#         return f(*args, **kwargs)
#     return inner

# @counter
# def add(a: int, b: int):
#     """Adds two values"""
#     return a + b

# @counter
# def mult(a, b):
#     return a*b

# Would get metadata from inner() if did not use functools.wraps
# print(help(add))