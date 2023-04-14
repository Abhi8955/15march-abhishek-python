string = "hello world, welcome to python programming"
substring = "o"

count = 0
for char in string:
    if char == substring:
        count += 1

print(f"The substring {substring} occurs {count} times in the string.")
