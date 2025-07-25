student_marks = {
    "alice": 85,
    "bob": 78, 
    "charlie": 92,
    "diana": 88, 
    "ethan": 74
}

student_name = input("Enter the student's name: ").strip().lower()

if student_name in student_marks:
    print(f"{student_name.title()}'s marks: {student_marks[student_name]}")
else:
    print(f"Sorry, no records found for '{student_name}'.")
