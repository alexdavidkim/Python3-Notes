# How does Python import modules?
    # No notes on it but watch 130:How does Python import modules? to see a custom importer
    # Checks sys.modules cache to see if the module has already been imported - if so it will use the memory reference there. Otherwise:
        # Creates a new module object (types.ModuleType is how you call a module instance)
        # Loads the source code from file
        # Adds an entry to sys.modules
        # Compiles and executes the source code

from types import ModuleType
import sys

def print_nice(obj):
    print('\n----------------------')
    if type(obj) == list:
        for i in obj:
            print(i)
    elif type(obj) == dict:
        for k,v in obj.items():
            print(k, v)
    print('----------------------\n')

# print_nice(sys.path)
# print_nice(sys.modules)

# See above for how Python imports modules. But after the first import, the memory location was already set for 'alex_module' so Python just referenced it again in memory. As opposed to the first time when it added the module to sys.modules cache
print('Running alex_module 1st time')
import alex_module
print('Running alex_module 2nd time')
import alex_module