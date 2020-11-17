# Lambdas are still from the function class
# The body of a lambda is limited to a single expression (not a single line of code)
# No assignments
# No annotations

# Without the lambda, sorted will yield ['B', 'C', 'a', 'd'] because of the ASCII character codes.
# my_list = ['B', 'a', 'C', 'd']
# print(sorted(my_list, key=lambda x: x.upper()))

# k represents the key so my_dict[k] will sort by values
# my_dict = {
#     'def': 300,
#     'abc': 200,
#     'ghi': 100
# }
# print(sorted(my_dict, key=lambda k: my_dict[k]))