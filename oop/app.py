class MyClass:
    names = ['alex', 'carmen', 'dean']

    def __init__(self, name):
        self.name = name

    def print_names(self):
        print(names)

    @staticmethod
    def static_print(*args):
        for arg in args:
            print(arg)

a = MyClass('baby')
a.static_print(None, True, 'sandwich', 100, [1,2,3])