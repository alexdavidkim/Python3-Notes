# Interning integers - Python caches a list of the integers [-5 ... 256] (inclusive) at startup that have their own memory addresses. This is for memory optimization. Any number outside this range will create a new object in memory and therefore c is not d == True. If you run this interning.py module vs running it directly in the Python interpreter, you will get different results. The reason for this is because Python compiles all the code, sees 2 integer values of equal value and assigns them to the same memory address at run time. For more, see the Q&A in Part 1 - Functional - Section 3-25 - 'Does Pycharm Implement this Optimization Differently?'
a = 10
b = 10
print(a is b)
# WARNING - see above
c = 257
d = 257
print(c is d)