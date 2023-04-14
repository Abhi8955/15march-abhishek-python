# swap two numbers using temporary variable

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swapping: a =", a, ", b =", b)

temp = a
a = b
b = temp

print("After swapping: a =", a, ", b =", b)



#------------------------------#


# swap two numbers without using temporary variable

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swapping: a =", a, ", b =", b)

a = a * b
b = a / b
a = a / b

print("After swapping: a =", a, ", b =", b)
