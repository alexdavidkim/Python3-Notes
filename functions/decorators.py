# The goal of a decorator is to store generic functionality to use across many different functions or classes!
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
# def counter(fn):
#     count = 0
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f'Function {fn.__name__} was called {count} times.')
#         return fn(*args, **kwargs)
#     return inner

# @counter
# def add(x, y):
#     return x + y

# add is no longer add but inner
# print(add.__name__)
# print(add(10, 20))
# print(add(30, 40))

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

# (Combined the videos in this section because we are sharing decorators)
# Application (Timer) - didn't finish
# Importing perf_counter in the decorator to make sure if it's used in another module, it will be imported there.
# Application (Logger, Stacked Decorators) - In practice, we would most likely log to an external .txt file. We would also have a separate module for this decorator and import to use wherever needed (which is again why we import our modules/functions inside the decorator).

# def logged(fn):
#     from datetime import datetime, timezone

#     def inner(*args, **kwargs):
#         run_datetime = datetime.now(timezone.utc)
#         result = fn(*args, **kwargs)
#         print(f'{run_datetime}: {fn.__name__}')
#         return result
#     return inner

# def timed(fn):
#     from time import perf_counter
    
#     def inner(*args, **kwargs):
#         start = perf_counter()
#         result = fn(*args, **kwargs)
#         end = perf_counter()
#         print(f'Function <{fn.__name__}> took {end - start} to run.')
#         return result
#     return inner  

# @logged
# @timed
# def fact(n):
#     from operator import mul
#     from functools import reduce

#     print('hello from factorial function')
#     return reduce(mul, range(1, n+1))

# print(fact(5))

# This is written this way to show how unwinding a stack can matter.
# See video for explanation if still not understood after the following:
    # @logged wraps the entire @timed + def fact(n) into it's fn param.
    # When we get to the 2nd line of logged, result = fn(), fn is executed. What is fn? fn is the entire timed + fact closure. 
    # So now we go to timed and it's fn param is fact
    # When we run timed's inner, and get to result = fn(), again we execute fact. I placed a print line there to show that this is indeed the first print statement that shows on the terminal.
    # Next we are still in inner so the next line is 'print(Function took blah blah)' so that is the 2nd print to the terminal
    # We then return to logged as timed has finished running
    # The next line of code to be executed in logged is 'print datetime name' which is the 3rd print to the terminal
    # Then we return the result which was the actual return value in fact
# All this to illustrate the importance of following the logic in a stack of function calls. This may not be a practical example but still something I want to be able to follow.
# See next blocks of code for a more simple version

# def dec_1(fn):
#     def inner():
#         result = fn()
#         print('Running decorator 1')
#         return result
#     return inner

# def dec_2(fn):
#     def inner():
#         result = fn()
#         print('Running decorator 2')
#         return result
#     return inner

# @dec_1
# @dec_2
# def my_func():
#     print('Running my_func')

# my_func()

# Steps -
    # dec_1 passes in dec_2(my_func) as it's parameter
    # Within dec_1's inner(), result = fn() calls fn() which is dec_2(my_func)
    # Within dec_2's inner(), result = fn() calls fn() which is my_func()
    # my_func is executed, print('Running my_func') to the terminal
    # Then we are back in dec_2's inner() and the next line of code is print('Running decorator 2') so that gets printed to the terminal
    # Then we are back in dec_1 inner which next line of code is print('Running decorator 1') so that gets printed to the terminal
    # KEY TAKEAWAY - result = fn() means that we are calling the function first (therefore going to another function) and then once that is executed, we go back to the original function

# Parameters in Decorators AND Decorator Factories
# outer(reps) is a decorator factory because it's not a decorator itself. It is returning a decorator, timed(fn). Remember: a decorator must take in a function as a parameter. What outer(reps) is doing here is allowing us to get more free variables into the closure. When we call @outer(10), we are calling timed(add), our inner function is doing things, returns those things to timed, and then timed is returned to outer.
# This is not how we would normally name the functions. Instead outer would be timed, and timed would be dec or similar. I just left it like this to prove the point that outer is not actually the primary decorator.

# def outer(reps):
#     def timed(fn):
#         from time import perf_counter

#         def inner(*args, **kwargs):
#             total_elapsed = 0
#             # pylint: disable=unused-variable
#             for i in range(reps):
#                 start = perf_counter()
#                 result = fn(*args, **kwargs)
#                 total_elapsed += (perf_counter() - start)
#             avg_elapsed = total_elapsed / reps
#             print(avg_elapsed)
#             return result
#         return inner
#     return timed

# @outer(10)
# def add(a, b):
#     return a + b

# Class Decorators - MyClass is the decorator factory where we can __init__ our free variables we want our decorator to have. __call__ allows our instances to be callable using obj() syntax. __call__ will be our decorator which takes in a function, does things within its inner function, then returns inner. @MyClass is creating an instance on the spot with 2 parameters as that is what is required.

# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def __call__(self, fn):
#         def inner(*args, **kwargs):
#             print(f'Calling {fn.__name__} with arguments: {self.a} {self.b}.')
#             return fn(*args, **kwargs)
#         return inner

# @MyClass(True, False)
# def my_func(s):
#     return f'Hello {s}.'

# print(my_func('world'))

# Decorator Application (Decorating Classes) - 7:113
# Goal: Make a decorator for many classes that will return debug info
# debug_info(obj) is our decorator. obj.debug points to info(self) which is a function that will return the debug information. Therefore, calling obj.debug() will call info(obj). We have to return the obj if we want to use @debug_info syntax because it is the same as Obj = debug_info(Obj) and if we don't return obj, it would be Obj = debug_info(None).
# Now we can use @debug_info on any class to access its functionality.

from datetime import datetime, timezone

def info(self):
    results = []
    results.append(f'time: {datetime.now(timezone.utc)}')
    results.append(f'Class: {self.__class__.__name__}') 
    results.append(f'id: {hex(id(self))}')
    for k, v in vars(self).items():
        results.append(f'{k}: {v}')
    return results

def debug_info(obj):
    obj.debug = info
    return obj

# @debug_info
# class Person:
#     def __init__(self, name, birth_year):
#         self.name = name
#         self.birth_year = birth_year

# p = Person('Zoe', 1987)
# print(p.debug())

# Just another example to show we can use debug_info on many different types of classes
# @debug_info
# class Automobile:
#     def __init__(self, make, model, year, top_speed, speed=0):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.top_speed = top_speed
#         self.speed = speed

#     @property
#     def speed(self):
#         return self._speed
    
#     @speed.setter
#     def speed(self, new_speed):
#         if new_speed > self.top_speed:
#             raise ValueError(f'Speed of {new_speed} can not exceed {self.top_speed}.')
#         else:
#             self._speed = new_speed

# auto1 = Automobile('Lexus', 'NX300', 2017, 140)
# print(auto1.speed)
# print(auto1.debug())

from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return f'Point: {self.x}, {self.y}'

    # Without __eq__, if we do p1 == p2, we get a False
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    # Without this - TypeError: '<' not supported between instances of 'Point' and 'Point'
    # Python is crazy... try '>'. You would think it wouldn't work because we haven't defined the method but it does because it just flips the operation for us since we have a '<' method.
    def __lt__(self, other):
        if isinstance(other, Point):
            return abs(self) < abs(other)
        else:
            return NotImplemented

    # But... to avoid the pain of creating __gt__, __le__, etc. We can make a decorator for all of them with the above 2 methods AND these assumptions:
        # a <= b if a < b or a == b
        # a > b if not(a < b) or a != b
        # a >= b if not(a < b)
    # Didn't finish this video but start at 34:00 if need to refer back

p1, p2, p3 = Point(2, 3), Point(2, 3), Point(0, 0)
print(p3 >= p1)
