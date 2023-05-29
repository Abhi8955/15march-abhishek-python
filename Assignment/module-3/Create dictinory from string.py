string = 'w3resource'

letter_count = {}

for char in string:
    letter_count[char] = letter_count.get(char, 0) + 1

print("Letter Count:", letter_count)
