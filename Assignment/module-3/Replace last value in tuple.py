def replace_last_value(tuples_list, new_value):
    updated_list = []
    for tup in tuples_list:
        updated_tup = tup[:-1] + (new_value,)
        updated_list.append(updated_tup)
    return updated_list
    
tuples_list = eval(input("Enter a list of tuples: "))
new_value = input("Enter the new value to replace the last value: ")

updated_list = replace_last_value(tuples_list, new_value)

print("Updated List of Tuples:")
for tup in updated_list:
    print(tup)
