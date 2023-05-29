def has_common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = input("Enter elements for the first list (comma-separated): ").split(",")
list1 = [item.strip() for item in list1]

list2 = input("Enter elements for the second list (comma-separated): ").split(",")
list2 = [item.strip() for item in list2]

result = has_common_member(list1, list2)
print("Do the lists have at least one common member?", result)
