def convert_to_string(char_list):
    string = ''.join(char_list)
    return string

input_chars = input("Enter characters for the list (no spaces): ")

char_list = list(input_chars)

result = convert_to_string(char_list)
print("Converted string:", result)
