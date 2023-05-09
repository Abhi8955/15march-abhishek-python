import counsellor_mangment as cm
import faculty_mangmant as fm



print("Welcome to our program!")
print("Please enter your role: counsellor, faculty, or student")
role = input("")

if role == "counsellor":
    while True:
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        print("5. Exit")
    
        choice = input("Enter your choice: ")
    
        if choice == "1":
            cm.add_student()
        elif choice == "2":
            cm.remove_student()
        elif choice == "3":
            cm.view_all_students()
        elif choice == "4":
            cm.view_specific_student()
        elif choice == "5":
        # Exit the program
            break
        else:
        # Display error message for invalid input
            print("Invalid choice!")

elif role == "faculty":
    while True:
        print("\nSelect an option:")
        print("1. Add marks for a student")
        print("2. View list of students")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            faculty_name = input("Enter your name: ")
            student_roll_no = input("Enter student roll no: ")
            marks = int(input("Enter marks to add: "))
            fm.add_student_marks(faculty_name, student_roll_no, marks)
        elif choice == 2:
            faculty_name = input("Enter your name: ")
            fm.view_students(faculty_name)
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

    
elif role == "student":
    print("Welcome, student! How can we help you succeed?")

else:
    print("Sorry, we do not recognize that role. Please try again.")