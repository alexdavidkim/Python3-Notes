                        # -------------- General -------------------

# To create runtime methods - see OOP - Section 2:18

class GeneralClass:
    def my_method(self):
        print('I am bound to my object which is the self parameter!')

    def my_function():
        print('I am not bound to my object because I am not a method! Therefore if you call me on an object, you will get an error!')

# general_obj = GeneralClass()
# print(type(GeneralClass.my_function), type(general_obj.my_method))

                        # ------ Built ins and introspection ------

# Use __dict__ to find the namespace of the state and behaviors objects

class BuiltInsClass:
    my_attr = 'I am a state, don\'t use me for behavior!'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Override me if you want a different string representation'    

    def __repr__(self):
        return 'Override me to show how I (the instance) was created, ex: BuiltInsClass(10,20)'

    def __call__(self):
        print("I'm being called from within __call__!")
        return 'Without me, you would not be able to call BuiltInsClass!'

# built_ins_obj = BuiltInsClass('Alex')
# print(BuiltInsClass.__dict__)
# print('\n-----------------\n')
# print(built_ins_obj.__dict__)

                    # --- Property Getters and Setters  ---

# The goal was to cache the area so we don't need to calculate it everytime the property was accessed

from math import pi

class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._area = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, new_radius):
        self._area = None
        self._radius = new_radius

    @property
    def area(self):
        if self._area is None:
            print('Calculating area...')
            self._area = pi * (self.radius ** 2)
        return self._area

                    # --- Class Methods  ---

# Why Class Methods?
    # When we want to call a method that only binds to the class but can be called on either the class or an instance.

class ClassMethod:

    @classmethod
    def help(cls):
        print(f'Call me from an instance or the class and my argument will always be: {cls}!')

                    # --- Static Methods  ---

# Why Static Methods?
    # They should be called static functions because we never want them bound.
    # Discouraged because the use cases are thin and if you want a function to be independent of the class or the instance, just move it to the module scope.

class StaticClass:

    @staticmethod
    def static_hello():
        print('You can call me from either the class or an instance and I will not be bound to either!')

StaticClass.static_hello()
static = StaticClass()
static.static_hello()