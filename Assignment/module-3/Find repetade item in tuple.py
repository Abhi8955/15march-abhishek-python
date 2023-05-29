def find_repeated_items(my_tuple):
    repeated_items = set()
    for item in my_tuple:
        if my_tuple.count(item) > 1:
            repeated_items.add(item)
    return repeated_items

my_tuple = eval(input("Enter a tuple of items: "))

repeated_items = find_repeated_items(my_tuple)

print("Repeated Items:", repeated_items)
