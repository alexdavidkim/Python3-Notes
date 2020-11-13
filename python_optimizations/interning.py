# Interning integers - Python caches a list of the integers [-5 ... 256] (inclusive) at startup that have their own memory addresses. This is for memory optimization. Any number outside this range will create a new object in memory and therefore c is not d == True. If you run this interning.py module vs running it directly in the Python interpreter, you will get different results. The reason for this is because Python compiles all the code, sees 2 integer values of equal value and assigns them to the same memory address at run time. For more, see the Q&A in Part 1 - Functional - Section 3-25 - 'Does Pycharm Implement this Optimization Differently?'
a = 10
b = 10
print(a is b)
# WARNING - see above
c = 257
d = 257
print(c is d)

# Interning strings - Generally not something done unless you really need to optimize your code for performance/memory. An example of a time to use string interning would be when you are dealing with the same string over and over. "this_string" == "this_string" is slow because you assess character by character. If you can intern certain strings, then you can use the is operator to compare memory addresses.
# If the string looks like an identifier, it will usually be interned. Identifier would be a string that has the same look to a variable, function or class name. 
a = 'hello'
b = 'hello'
print(a is b)
# This should be false but see above note on the compiler. This should be false because 'hello world' does not look like an identifier.
c = 'hello world'
d = 'hello world'
print(c is d)
e = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
f = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
print(e is f)
# To see how to use the sys.intern() method to create our own interning of strings, see Part 1 - Functional - Section 3:26