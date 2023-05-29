my_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15, 'e': 25}

sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)

highest_values = [value for key, value in sorted_items[:3]]

print("Highest 3 Values:", highest_values)
