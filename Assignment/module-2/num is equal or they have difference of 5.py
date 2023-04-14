a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

if a == b or (a - b == 5) or (b - a == 5) or (a + b == 5):
    print("True")
else:
    print("False")
