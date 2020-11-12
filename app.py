my_var_1 = 10
my_var_2 = 10

def change_var(x):
    print(id(x))
    print(id(my_var_2))
    x == None
    print(id(x))
    print(id(my_var_2))

change_var(my_var_1)