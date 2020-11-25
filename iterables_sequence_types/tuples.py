# Need to appreciate tuples like strings. Strings are only useful if the elements (characters) are in a certain order.
    # Super useful as data structures:
        # Think of a point on a graph, (10, 20). Represents exactly one location, x=10, y=20.
        # Data structures are an agreed upon meaning to data in a structure. 
            # london = ('London', 'UK', 8_780_000) is a data structure represented as a tuple where it provides meaning to those who know the "code": (city, country, population)
# Tuples are immutable: fixed length, fixed order 
    # The "exception" to this is when a mutable object, such as a list, is an element of the tuple. In this case, we could change the contents of the list and it would appear changed in the tuple (even though the memory address for the list stays the same).
# my_list = [1,2,3]
# my_tuple = (1, None, my_list)
# my_list = [1,2,3,4]
# print(my_list)
# print(my_tuple)

# The () to create a tuple are not required but suggested. What really designates a tuple is a comma. The only exception is when you want to create an empty tuple.
# a = 1,2,3
# print(type(a))
# b = ()
# print(type(b))
# c = (1)
# print(type(c))
# d = (1,)
# print(type(d))

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y})'

point = Point2D(10, 20)
print(point)
print(hex(id(point)))
point.x = 100
print(point)
print(hex(id(point)))