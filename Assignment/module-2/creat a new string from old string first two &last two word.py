def get_new_string(s):
    if len(s) < 2:
        new_string = ""
    else:
        new_string = s[:2] + s[-2:]
    print(new_string)

# Example usage:
get_new_string("Hello")
get_new_string("H")
