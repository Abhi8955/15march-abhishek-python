def find_second_smallest(numbers):
    if len(numbers) < 2:
        return "List should have at least two elements."
    
    smallest = float('inf')
    second_smallest = float('inf')
    
    for num in numbers:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    if second_smallest == float('inf'):
        return "There is no second smallest element in the list."
    else:
        return second_smallest

number_list = input("Enter numbers for the list (comma-separated): ").split(",")

number_list = [int(num.strip()) for num in number_list]

result = find_second_smallest(number_list)
print("Second smallest number:", result)
