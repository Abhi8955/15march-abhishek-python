def remove_empty_tuples(tuples_list):
    updated_list = [tup for tup in tuples_list if tup]
    return updated_list

tuples_list = eval(input("Enter a list of tuples: "))

updated_list = remove_empty_tuples(tuples_list)

print("Updated List of Tuples:")
for tup in updated_list:
    print(tup)
