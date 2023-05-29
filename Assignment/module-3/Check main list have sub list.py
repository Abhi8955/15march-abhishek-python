main_list = input("Enter elements for the main list (comma-separated): ").split(",")
sub_list = input("Enter elements for the sub-list (comma-separated): ").split(",")

main_list = [item.strip() for item in main_list]
sub_list = [item.strip() for item in sub_list]

if set(sub_list).issubset(main_list):
    print("The main list contains the sub-list.")
else:
    print("The main list does not contain the sub-list.")
