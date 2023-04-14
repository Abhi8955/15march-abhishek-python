string = input("Enter a string: ")
char_frequency = {}

for char in string:
    char_frequency[char] = char_frequency.get(char, 0) + 1
for char, freq in char_frequency.items():
    print(char, ":", freq)
