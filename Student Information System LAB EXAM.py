info = ['Student ID No.', 'First Name', 'Last Name', 'Course', 'Year Level', 'Contact No.', 'Email']

students = []

def add_student():
    if len(students) >= 10:
        print("Maximum of 10 students reached. Cannot add more.")
        return
    
    student = []
    student.append(input("\nEnter Student ID No.: "))
    student.append(input("Enter First Name: "))
    student.append(input("Enter Last Name: "))
    student.append(input("Enter Course: "))
    student.append(input("Enter Year Level: "))
    student.append(input("Enter Contact No.: "))
    student.append(input("Enter Email: "))
    
    students.append(student)
    print("\033[33mStudent added successfully!\033[0m")

def search_student():
    if not students:
        print("No students in the system.")
        return
    
    search_id = input("\nEnter Student ID No. to search: ")
    for student in students:
        if student[0] == search_id:
            print("\033[33m\nStudent Details:\033[0m")
            for i in range(len(student)):
                print(f"{info[i]}: {student[i]}")
            return
    print("\033[31mStudent not found.\033[0m")

def view_all_students():
    if not students:
        print("\033[33m\nNo students in the system.\033[0m")
        return
    
    print("\033[33m\nAll Students:\033[0m")
    for student in students:
        print(f"ID: {student[0]}, Last Name: {student[2]}")

def menu():
    while True:
        print("\033[32m\nStudent Information System\033[0m")
        print("1. Add Student")
        print("2. Search Student")
        print("3. View All Students")
        print("4. Exit")
        choice = input("Choice:")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            print("\033[33mExiting the system.\033[0m")
            break
        else:
            print("\033[31mInvalid choice. Please try again.\033[0m")

if __name__ == "__main__":
    menu()