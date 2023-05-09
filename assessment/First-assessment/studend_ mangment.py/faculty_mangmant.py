import datetime

students = [
    {"name": "abhi", "roll_no": "101", "marks": 0, "faculty": "dev"},
    {"name": "rakesh", "roll_no": "102", "marks": 0, "faculty": "dev"},
    {"name": "piyush", "roll_no": "103", "marks": 0, "faculty": "dev"}
]

def view_students(faculty_name):
    print(f"List of students for {faculty_name}:")
    for student in students:
        if student["faculty"] == faculty_name:
            print(f"Name: {student['name']}, Roll No: {student['roll_no']}, Marks: {student['marks']}")

def add_student_marks(faculty_name, student_roll_no, marks):
    for student in students:
        if student["roll_no"] == student_roll_no and student["faculty"] == faculty_name:
            student["marks"] = marks
            transaction_log = f"{faculty_name} added marks for student {student['name']} with roll no {student_roll_no} on {datetime.datetime.now()}"
            with open("transaction_log.txt", "a") as f:
                f.write(transaction_log)
            print("Marks added successfully!")
            return
    print("Error: Student with this roll no not found or you don't have access to this student.")

