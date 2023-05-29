def get_unique_values(lst):
    unique_values = list(set(lst))
    return unique_values

input_list = input("Enter elements for the list (comma-separated): ").split(",")
input_list = [item.strip() for item in input_list]

result = get_unique_values(input_list)
print("Unique values:", result)
