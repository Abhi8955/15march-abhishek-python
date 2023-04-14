a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

if a == b or b == c or c == a:
    print("Two of the numbers are equal, so the sum is zero.")
    sum = 0
else:
    sum = a + b + c
    print("The sum of the three numbers is:", sum)
