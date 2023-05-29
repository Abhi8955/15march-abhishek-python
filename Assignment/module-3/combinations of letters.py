data = {'1': ['a', 'b'], '2': ['c', 'd']}

values = list(data.values())

combinations = []

for letter1 in values[0]:
    for letter2 in values[1]:
        combinations.append(letter1 + letter2)

for combination in combinations:
    print(combination)
