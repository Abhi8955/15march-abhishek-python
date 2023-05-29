def is_palindrome(string):
    string = ''.join(char.lower() for char in string if char.isalnum())

    return string == string[::-1]
string = "Madam"
if is_palindrome(string):
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
