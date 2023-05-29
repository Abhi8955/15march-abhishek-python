def split_list(my_list):
    if len(my_list) < 3:
        return "List should have at least three elements."
    else:
        first, *middle, last = my_list
        return first, middle, last

input_list = input("Enter elements for the list (comma-separated): ").split(",")

input_list = [item.strip() for item in input_list]

result = split_list(input_list)

print("First:", result[0])
print("Middle:", result[1])
print("Last:", result[2])
