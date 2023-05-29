dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

merged_dict = dict1.copy() 
merged_dict.update(dict2)  
 
print("Merged Dictionary (update()):", merged_dict)

merged_dict2 = {**dict1, **dict2}

print("Merged Dictionary ({**dict1, **dict2}):", merged_dict2)
