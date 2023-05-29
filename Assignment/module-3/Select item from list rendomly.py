import random

def select_random_item(item_list):
    random_item = random.choice(item_list)
    return random_item

my_list = [1, 2, 3, 4, 5]
result = select_random_item(my_list)
print("Randomly selected item:", result)
