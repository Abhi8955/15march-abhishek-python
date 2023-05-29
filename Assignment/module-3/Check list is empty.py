def is_list_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False

my_list = [] 
result = is_list_empty(my_list)
print("Is the list empty?", result)
