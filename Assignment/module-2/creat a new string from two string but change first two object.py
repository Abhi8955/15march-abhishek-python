string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

new_string = string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]

print("The new string is:", new_string)
