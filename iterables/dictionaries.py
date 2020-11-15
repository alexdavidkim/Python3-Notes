# Dictionaries are unordered.

my_dict = {
    'key1': 1,
    'key2': None,
    'key3': 3.14,
    'key4': [1,2,3],
}
# Iterate over keys
# for x in my_dict:
#     print(x)

# Iterate over values
# for x in my_dict.values():
#     print(x)

# Unpacking values
# a, b, c, d = my_dict.values()
# print(a, b, c, d)

# Unpacking each tuple in the dictionary
# for t in my_dict.items():
#     print(t)

# Unpacking key, value pairs
# for k, v in my_dict.items():
#     print(k, v)

# ** unpacks k/v pairs into another dictionary. Can only be used on the right hand side. Notice how 'h':5 overwrode 'h':4.
my_dict_1 = {'p': 1, 'y': 2}
my_dict_2 = {'t': 3, 'h': 4}
my_dict_3 = {'h': 5, 'o': 6, 'n': 7}
merged_dict = {**my_dict_1, **my_dict_2, **my_dict_3}
print(merged_dict)