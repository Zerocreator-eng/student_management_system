Students = []
class Student:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course

def add_student():
    id = input("Enter student ID: ")
    for s in Students:
        if s.id == id:
            print("Student ID already exists")
            return
    name = input("Enter student Name: ")
    try:
        age = int(input("Enter student Age: "))
    except ValueError:
        print("Invalid Age")
        return
    course = input("Enter student Course: ")
    student = Student(id, name, age, course)
    Students.append(student)
    print("Student added sucessfully")

def view_students():
    if len(Students) == 0:
        print("No student found")
    else:
        print("\nStudent_list")
        for i, student in enumerate(Students,  start=1):
            print(i, student.id, student.name, student.age, student.course)
def search_student():
    name = input("Enter student name to search: ").lower()
    found = False

    for student in Students:
        if name in student.name.lower():
            print(student.id, student.name, student.age, student.course)
            found = True
    if not found:
        print("Student name not found")
def update_student():
    id = input("Enter student ID to update: ")
    for student in Students:
        if student.id == id:
            print("press Enter if not updating")

            new_name = input("Enter student name: ")
            new_age = input("Enter student Age: ")
            new_course = input("Enter student Course: ")

            if new_name:
                student.name = new_name
            if new_age:
                try:
                    student.age = int(new_age)
                except ValueError:
                    print("Invalid Age, keeping the old value")
            if new_course:
                student.course = new_course
            print("Student updated successfully")
            return
    print("Student not found")

def delete_student():
    id = input("Enter student ID to delete: ")
    for student in Students:
        if student.id == id:
            Students.remove(student)
            print("Student deleted sucessfully")
            return
    print("Student not found")

def count_students():
    print("total students: ", len(Students))


while True:
    print("\nStudents list")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Students")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. count students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        count_students()
    elif choice == "7":
        print("Thank you for using this program")
        break
    else:
        print("Invalid choice")






