def count_strings(strings):
    count = 0
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

string_list = input("Enter a list of strings (comma-separated): ").split(",")

string_list = [string.strip() for string in string_list]

result = count_strings(string_list)
print("Number of strings meeting the criteria:", result)
