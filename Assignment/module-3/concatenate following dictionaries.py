dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

new_dict = {}

new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print("Concatenated Dictionary:", new_dict)
