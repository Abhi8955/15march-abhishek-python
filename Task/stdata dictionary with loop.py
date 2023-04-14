
students = {}

num_students = int(input("enter the number of students:"))

for i in range(num_students):
    print(f"Enter information for student {i+1}:")
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    
    student_info = {"Name": name, "Age": age, "Grade": grade}
    
    students[f"Student {i+1}"] = student_info

print(students)
