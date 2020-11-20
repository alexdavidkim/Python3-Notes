# Closures - Part 1 - Functional - Section 7:101
# Closures are simply a function plus an extended scope that contains the free variables not defined within the function. Think of closures as a function that can be stored as a variable with free, hidden variables.

# ***
# Think of closures like this. It is literally the same thing as commenting out def averager(): and return add. But then it would be a global variable of numbers. This is a good way to: 
    # - Hide variables in a local scope so it can't be erroneously modified later.
    # - Create multiple "instances" (f1, f2, f3 - all with same functionality but pointing to different cells)

# def averager():

#     total = 0
#     count = 0
#     def add(number):
#         nonlocal total
#         nonlocal count
#         total += number
#         count += 1
#         return total / count

#     return add


# Deep Dive - Python creates an intermediary object (cell) between the shared variables that have different scopes and the object in memory they are pointing to. In the example below, inner_func AND x = 'x in closure' are the components of the closure. When inner_func is returned, one might think it would throw an error when called because it's referencing a variable x that is not defined in its scope. But it is. x is a free variable that is part of the closure. inner_func's x AND outer_func's x both point to the intermediary cell object. That cell object points to the type string value 'x in closure' (inner_func x AND outer_func x) -> cell object -> 'x in closure'. So even though outer_func x isn't pointing to the cell object after execution, inner_func x is and therefore still has access. Cells are required because they keep the variables pointing at the same memory address. Example: strings are immutable so if you changed x in one location, you want the closure to change it in all locations but wouldn't without a cell.
# x = 'x in module scope'
# def outer_func():
    #pylint: disable=unused-variable
    # a = 100
    # x = 'x in closure'
    # def inner_func():
        # print(x)
    # return inner_func
# fn is referencing a CALLED outer_func() which has a return value of an UNCALLED inner_func. So fn is an uncalled inner_func and we just call it to execute inner_func() and x is still accessed because it is part of the closure.
# fn = outer_func()
# fn()

# Tricks - 
# Returns a tuple with all free variables.
# print(fn.__code__.co_freevars) 
# Shows the cell object and where it's pointing to.
# print(fn.__closure__) 

# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# fn = counter()
# print(fn())
# print(fn())

# f1 and f2 both create different instances of the closure and cell, even though they both point to the singleton object of 0. The opposite is the next example.
# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment
# f1 = counter()
# f2 = counter()
# print(f1())
# print(f1())
# print(f2())
# print(f2())
# print(f1.__closure__)
# print(f2.__closure__)

# Closures are created at compile time. So inner_func_1 and 2 are both created and pointing to the same cell. This allows them to both use the same count free variable
# def counter():
#     count = 0
#     def inner_func_1():
#         nonlocal count
#         count += 1
#         return count
#     def inner_func_2():
#         nonlocal count
#         count += 1
#         return count
#     return inner_func_1, inner_func_2
# f1, f2 = counter()
# print(f1())
# print(f2())
# print(f1())
# print(f2())
# The desired output may have been 11, 12, 13 however we get 13, 13, 13. adder is an empty list. The for loop takes in n in range 1,2,3 so n should be 1,2,3. This is technically not a closure because n is a global variable. One of the main features of a closure is to have free LOCAL variables.
# adders = []
# for n in range(1,4):
#     adders.append(lambda x: x + n)
# print(adders[0](10))
# print(adders[1](10))
# print(adders[2](10))
# To solve above - 7:102 27:50 mark - First we have to wrap the logic in a function because this will create a closure with a LOCAL free variable. Then the magic trick is this: if the lambda stayed the same as above, the results would still be 13, 13, 13 and that is because while each element in adders is a closure, they all share the same cell which points to 13 as that was the last iteration in the loop. With y=n, we are setting a default parameter y that is equal to 1, 2, and then 3. The reason this works is because we are capturing each individual n value BEFORE appending to adders. The irony is this is actually not even a closure anymore because we aren't using the free variable.
# def create_adders():
#     adders = []
#     for n in range(1, 4):
#         adders.append(lambda x, y=n: x + y)
#     return adders
# adders = create_adders()
# print(adders[0](10))
# print(adders[1](10))
# print(adders[2](10))

# fn returns inner function unexecuted. inner returns inc function unexecuted. inc() is a closure with 2 free variables: n, start. So essentially what the nested incrementer function does is take n which is how much to increment by, start which specifies a starting number, and then inc() performs the work of start += n. To implement this nested function, we create fn which returns inner. Then we create our final function increment_by_2_start_100 by making it = fn(100).
# def incrementer(n):
#     def inner(start):
#         def inc():
#             nonlocal start
#             start += n
#             return start
#         return inc
#     return inner
# fn = incrementer(2)
# increment_by_2_start_100 = fn(100)
# print(increment_by_2_start_100())
# print(increment_by_2_start_100())
# print(increment_by_2_start_100())

# Applications Part 1 
# def averager():
#     total = 0
#     count = 0
#     def add(number):
#         nonlocal total
#         nonlocal count
#         total += number
#         count += 1
#         return total / count
#     return add
# f1 = averager()
# print(f1(20))
# print(f1(40))

# You can write the above as a class
# class Averager():

#     def __init__(self):
#         self.total = 0
#         self.count = 0

#     def add(self, number):
#         self.total += number
#         self.count += 1
#         return self.total / self.count
    
# a = Averager()
# print(a.add(10))
# print(a.add(20))