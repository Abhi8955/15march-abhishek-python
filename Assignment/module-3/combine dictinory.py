from collections import Counter

data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

combined_values = Counter()

for dictionary in data:
    item = dictionary['item']
    amount = dictionary['amount']
    combined_values[item] += amount

print("Combined Values:", combined_values)
