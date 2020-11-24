def decorator(fn):

    def inner(*args, **kwargs):
        print(f'Print before {fn.__name__} runs.')
        result = fn(*args, **kwargs)
        print(f'Print after {fn.__name__} runs.')
        return result
    return inner

@decorator
def my_func():
    print('I am my_func!') 
    return 'I am my_func returned!'

print(my_func())