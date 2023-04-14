def insert_string_in_middle(original_string, string_to_insert):

    mid = len(original_string) // 2
    original_string = original_string[:mid] + string_to_insert + original_string[mid:]
    print(original_string)
