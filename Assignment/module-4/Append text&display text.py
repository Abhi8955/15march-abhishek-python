def append_text_to_file(file_path, text):
    try:
        with open(file_path, 'a') as file:
            file.write(text)
        print("Text appended successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

file_path = input("Enter the path of the file: ")
text_to_append = input("Enter the text to append: ")

append_text_to_file(file_path, text_to_append)

try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print("Updated File Contents:")
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
