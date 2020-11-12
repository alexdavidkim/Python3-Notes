import sys, ctypes

# Part 1 - Section 3 - Reference Counting

a = [1,2,3]

# By calling sys.getrefcount() it adds an additional pointer to the memory address for variable a. So by default, this will add 1 to the reference count always
print(sys.getrefcount(a))

# We could call the returned block of code directly, however we we want to pass in an actual memory address to the function to make it easier here. The reason this returns the correct reference count is because Python first runs id(a), this value is assigned as the parameter to ref_count() and then dropped as a memory reference. With getrefcount(), the function is still using the variable a so it's counting it towards the count
def ref_count(address):
    return ctypes.c_long.from_address(address).value
print(ref_count(id(a)))

