# https://realpython.com/python-scope-legb-rule/#:~:text=The%20local%20scope%20or%20function,blueprint%20for%20new%20local%20scopes.

# global keyword can be used to create a global variable from within a function. If the variable already exists, it will override the reference globally. If not in existence, it will create a new pointer. The global keyword doesn't change the global variable until the function has been invoked.
# a = True
# def my_func():
#     global a
#     a = False
#     print(a)
# my_func()
# print(a)
# def my_func():
#     global foo 
#     foo = None
#     print(foo)
# my_func()

# UnboundLocalError: local variable 'a' referenced before assignment
# When Python compiles the code, it creates a function object and this function object says that a has local scope. Therefore, at runtime when my_func tries to access a in the first line of the function, my_func is looking for a on a local scope and can not find it. What this tells us about Python is that it assigns the scope of variables inside functions at compile time, but does not compute the reference until runtime. Part 1 - Functional - Section 7:98
# a = 10
# def my_func():
#     print('Global a:', a)
#     a = 'hello world'
#     print(a)
# my_func()

# UnboundLocalError: local variable 'foo' referenced before assignment
# Python looks at my_func and sees variable foo being assigned so when it compiles, it's associating foo as a local variable NOT a global variable. At run time, print(foo) is run before foo is assigned to 200 and therefore hit an error.
# foo = 100
# def my_func():
#     print(foo)
#     foo = 200
# my_func()

# Illustrates the cascading nature of scopes from local to built in
# foo = [1,2,3]
# def outer_func():
#     a = 100
#     b = 'I am b'
#     def inner_func():
#         a = 10
#         print(f'inner func -> a: {a}')
#         print(f'inner func -> outer_func -> b: {b}')
#         print(f'inner_func -> outer_func -> global scope -> foo: {foo}')
#     inner_func()
#     print(f'outer_func -> a: {a}')
# outer_func()

# Interesting in 3 ways:
# nonlocal keyword tells Python that the scope of x being assigned in inner_func is not local, therefore it moves up the cascade and exists in the outer_func scope (nonlocal will NOT look in the global scope, only the enclosing local scopes). If you comment out nonlocal x, x = 'bye bye' only exists in the inner_func scope, so even when inner_func is called on the next line, x is still = 'hello'.
# If you do not call inner_func(), even though inner_func is compiled, it was never run and therefore x = 'hello'.
# def outer_func():
#     x = 'hello'
#     def inner_func():
#         nonlocal x
#         x = 'bye bye'
#     inner_func()
#     print(x)
# outer_func()

# Modifying variables outside inner scope
# inner2 is able to modify inner1.x to 'monty' BUT only after it is called. So 'inner(before): x' is going to have x = 'python'. Then inner2() is called thus completing the reassignment. Then 'inner(after): x' will be 'monty'. inner1() has already been called which is what was written before. Then because inner1 does not modify outer.x with the nonlocal keyword, x is just still 'hello'.
# def outer():
#     x = 'hello'
#     def inner1():
#         x = 'python'
#         def inner2():
#             nonlocal x
#             x = 'monty'
#         print('inner(before):', x)
#         inner2()
#         print('inner(after):', x)
#     inner1()
#     print('outer:', x)
# outer()