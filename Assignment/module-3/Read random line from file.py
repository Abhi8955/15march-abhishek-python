import random

file_path = 'path/to/file.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines)
    print(random_line.strip())

