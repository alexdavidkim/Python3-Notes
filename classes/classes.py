# Overwriting dunder methods for our own functionality is a key feature included with Python
# Getters and setters - 'Part 1 - Section 2 - Classes - 27:50'. 
# See 'classes/property_dec.py' for a simple explanation/Youtube video 
# In the __init__ method, we are actually calling the setter method decorated by @width.setter. We do this to allow the custom case of ValueError's being raised when an object is created with length or width <= 0. 
# Here are the steps an instance takes:
    # r1 = Rectangle(10, 20) passes in 10, 20 to the __init__ method in Rectangle class
    # self.width and self.height both reference their setter methods (Going forward we will use width as the example)
    # def width(self, width) - takes in 10. If 10 <= 0, raise ValueError, else, self._width = width. So the only way to access this private variable, _width, is through the setter function.
        # @width_setter along with @property are built-in decorators that allow us to get and set attributes with this syntax: OBJ.name or OBJ.name = 'name'
    # Now if we want to Get the width, @property allows us to say, r1.width, which returns self._width

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     @property
#     def width(self):
#         return self._width
    
#     @width.setter
#     def width(self, width):
#         if width <= 0:
#             raise ValueError('Width must be positive')
#         else:
#             self._width = width

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self, height):
#         if height <= 0:
#             raise ValueError('Height must be positive')
#         else:
#             self._height = height

#     def area(self):
#         return self.width * self.height

    # The built in __str__ method usually prints out the class and memory location of an object
    # def __str__(self):
    #     return f'Rectangle: width={self.width}, height={self.height}'

    # __repr__ usually prints out how an object was created
    # def __repr__(self):
    #     return f'Rectangle({self.width}, {self.height})'

    # # __eq__ is represented as 'r1 == r2' where r1 is self, == is __eq__, and r2 is other. Watch 'Part 1 - Section 2 - Classes - 15:11' for an explanation of isinstance() being used below
    # def __eq__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.width == other.width and self.height == other.height 
    #     else:
    #         return False

    # # # __lt__ is less than. See documentation for __gt__, __le__, etc. As the programmer, we are deciding how to define the comparison operator of less than. We could choose to make it anything we want. Beautiful!
    # def __lt__(self, other):
    #     if isinstance(other, Rectangle):
    #         return self.area() < other.area()
    #     else:
    #         return NotImplemented # See '/built_in_constants.py'

# r1 = Rectangle(10, 20)
# r2 = Rectangle(10, 20)
# r3 = Rectangle(100, 200)

# print(str(r1))
# print(repr(r1))
# print(r1 is not r2)
# print(r1 == r2)
# print(r1 < r3)

# Callables - classes are callable. Instances of classes are not unless you specifiy them to be with __call__. Part 1 - Functional - Section 6:87
# class MyClass():
#     def __init__(self, x=0):
#         print('Initialized an instance of MyClass')
#         self.counter = x

#     def __call__(self, x=1):
#         print(f'Incrementing counter by: {x}')
#         self.counter += x

# a = MyClass()
# print(callable(a))
# a(10)
# print(a.counter)