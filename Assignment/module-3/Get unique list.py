def get_unique_elements(lst):
    unique_list = list(set(lst))
    return unique_list

input_list = input("Enter elements for the list (comma-separated): ").split(",")

input_list = [item.strip() for item in input_list]

result = get_unique_elements(input_list)
print("Unique elements of the list:", result)
