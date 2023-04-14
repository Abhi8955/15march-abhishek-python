def add_suffix(word):
    if len(word) < 3:
        result = word
    elif word[-3:] == 'ing':
        result = word + 'ly'
    else:
        result = word + 'ing'
    print(result)

# Example usage
add_suffix('swim')
add_suffix('swimming')
add_suffix('hi')
