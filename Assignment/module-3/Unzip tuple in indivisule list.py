my_list = [(1, 'a'), (2, 'b'), (3, 'c')]

unzipped_list = list(zip(*my_list))

first_list = list(unzipped_list[0])
second_list = list(unzipped_list[1])

print("First List:", first_list)
print("Second List:", second_list)
