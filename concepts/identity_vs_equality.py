# is is the identity operator. It compares the memory address of 2 objects. var_1 and var_2 are the equal, proven by the == equality operator. However, they are not pointing to the same object. The reverse is true with 'is not' and '!='.
# var_1 = [1,2,3]
# var_2 = [1,2,3]
# print(var_1 is var_2)
# print(var_1 == var_2)
# var_2.append(4)
# print(var_1 == var_2)

# a is an int and b is a float so they do not point to the same memory address. However, Python figures out they are of equal value. Python also figures out c, which is 20 - 10 is of the same value as well.
# a = 10
# b = 10.0
# print(a is b)
# print(a == b)
# c = 20 - 10
# print(c == a)

# None is an object with a shared reference. All variables pointing to None will share the same reference. None is used as a placeholder to indicate they are an empty value not set yet, generally.
# a = None
# b = None
# c = None
# print(a is b is c)
# x = 10
# print(x is not None)