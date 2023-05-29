def check_range(number, start, end):
    if start <= number <= end:
        return True
    else:
        return False
number = 15
start = 10
end = 20

if check_range(number, start, end):
    print(f"{number} is in the range [{start}, {end}].")
else:
    print(f"{number} is not in the range [{start}, {end}].")
