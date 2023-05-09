import pprint
# Initialize the nested dictionary to store student information
students = {}

# Function to add a new student
def add_student():
    while True:
        try:
            student_id = input("Enter student ID: ")
            
            # Input for name
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            name = {"first_name": first_name, "last_name": last_name}
            
            # Input for age
            age = int(input("Enter age: "))
            
            # Input for contact
            contact_number = input("Enter contact number: ")
            contact = {"number": contact_number}
            
            # Initialize the subjects dictionary
            subjects = {}
            
            # Input for subjects and faculty
            num_subjects = int(input("Enter the number of subjects: "))
            for i in range(num_subjects):
                subject_name = input("Enter subject name: ")
                subject_fee = float(input("Enter subject fee: "))
                subject_marks = float(input("Enter subject marks: "))
                
                faculty_name = input("Enter faculty name: ")
                
                subject_details = {"fee": subject_fee, "marks": subject_marks, "faculty_name": faculty_name}
                
                subjects[subject_name] = subject_details
            
            # Create the student dictionary
            student = {
                "name": name,
                "age": age,
                "contact": contact,
                "subjects": subjects
            }
            
            # Add the student to the nested dictionary
            students[student_id] = student
            
            print("Student added successfully!")
            
            # Print the added student data
            print("Added Student Data:")
            print("Student ID:", student_id)
            print("Name:", first_name, last_name)
            print("Age:", age)
            print("Contact Number:", contact_number)
            print("Subjects:")
            for subject, subject_details in subjects.items():
                print("Subject:", subject)
                print("Fee:", subject_details["fee"])
                print("Marks:", subject_details["marks"])
                print("Faculty Name:", subject_details["faculty_name"])
            
            # Print the entire nested dictionary
            print("Updated Student Data:")
            pprint.pprint(students)
            
            break
            
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print("An unexpected error occurred:", e)

# Function to remove a student
def remove_student():
    while True:
        try:
            # Accept input from user for the student ID to be removed
            student_id = input("Enter student ID to remove: ")
            
            # Check if the student ID exists in the nested dictionary
            if student_id in students:
                # Remove the student from the nested dictionary
                del students[student_id]
                print("Student removed successfully!")
                break
            else:
                print("Student not found!")
                
        except Exception as e:
            print("An unexpected error occurred: ", e)

# Function to view all students
def view_all_students():
    # Iterate over each student in the nested dictionary and print their details
    for student_id, student in students.items():
        print("Student ID: ", student_id)
        print("First Name: ", student["first_name"])
        print("Last Name: ", student["last_name"])
        print("Age: ", student["age"])
        print("Contact Number: ", student["contact_number"])
        print("Subjects: ")
        for subject, grade in student["subjects"].items():
            print("\t", subject)
        print("Fees: ")
        for subject, fee in student["fees"].items():
            print("\t", subject, ": $", fee)

# Function to view a specific student
def view_specific_student():
    while True:
        try:
            # Accept input from user for the student ID to be viewed
            student_id = input("Enter student ID to view: ")
            
            # Check if the student ID exists in the nested dictionary
            if student_id in students:
                # Get the student details from the nested dictionary
                student = students[student_id]
                
                # Print the student details
                print("Student ID: ", student_id)
                print("First Name: ", student["first_name"])
                print("Last Name: ", student["last_name"])
                print("Age: ", student["age"])
                print("Contact Number: ", student["contact_number"])
                print("Subjects: ")
                for subject, grade in student["subjects"].items():
                    print("\t", subject)
                print("Fees: ")
                for subject, fee in student["fees"].items():
                    print("\t", subject, ": $", fee)
                    
                break
            else:
                print("Student not found!")
                
        except Exception as e:
            print("An unexpected error occurred: ", e)

