my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}

unique_values = set()

for value in my_dict.values():
    unique_values.add(value)

print("Unique Values:", unique_values)
