def generate_square_list(start, end):
    square_list = [num ** 2 for num in range(start, end+1)]
    first_five = square_list[:5]
    last_five = square_list[-5:]
    return first_five + last_five

start_num = int(input("Enter the start number: "))
end_num = int(input("Enter the end number: "))

result_list = generate_square_list(start_num, end_num)

print("First and last 5 elements of the square list:")
for num in result_list:
    print(num)
