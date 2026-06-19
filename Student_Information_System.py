info = ['Student ID No.', 'First Name', 'Last Name', 'Course', 'Year Level', 'Email', 'Contact No.']

students = []
archived_students = []

def add_student():
    print("\n====== ADD STUDENT ======")
    student_id = input("Enter Student ID No.: ")

    for student in students:
        if student[0] == student_id:
            print ("A Student with this ID No. already exists.")
            return
    
    student = [student_id]
    student.append(input("Enter First Name: "))
    student.append(input("Enter Last Name: "))
    student.append(input("Enter Course: "))
    student.append(input("Enter Year Level: "))
    student.append(input("Enter Email: "))
    student.append(input("Enter Contact No.: "))

    students.append(student)
    print("\nStudent Added Successfully!\n")

def search_student():
    if not students:
        print("\nNo Students in the System!")
        return
    
    search_id = input("Enter Student ID No.: ")
    for student in students:
        if student[0] == search_id:
            print("\n==== STUDENT DETAILS ====")
            for i in range(len(student)):
                print(f"{info[i]}: {student[i]}")
            return
    print("Student Not Found!")

def view_all_students():
    if not students:
        print("\nNo Students in the System!")
        return
    
    print("\n------- STUDENT LIST -------")
    for student in students:
        print(f"ID No.: {student[0]}, Last Name: {student[2]}")

def edit_student():
    if not students:
        print("\nNo Students in the System!")
        return
    
    search_id = input("Enter Student ID No.: ")
    for student in students:
        if student[0] == search_id:
            print("Leave a blank field to keep current value.")
            for i in range(1, len(student)):

                new_value = input(f"{info[i]}, [{student[i]}]: ")
                if new_value:
                    student[i] = new_value
            print("\nUpdated Successfully!")
            return
    print("\nStudent not Found.")

def delete_student():
    if not students:
        print("\nNo Students in the System!")
        return

    search_id = input("Enter Student ID No.: ")
    for student in students:
        if student[0] == search_id:
            confirm = input(f"Move {student[1]} {student[2]} to Archive? (y/n): ")
            if confirm.lower() == 'y':
                students.remove(student)
                archived_students.append(student)
                print("\nStudent Archived Successfully!")
            else:
                print("Deletion Cancelled.")
            return
    print("\nStudent Not Found.")

def view_archive():
    if not archived_students:
        print("No Archived Students.")
        return
    
    print("\n===== ARCHIVED STUDENTS =====")
    for student in archived_students:
        print(f"ID No.: {student[0]}, Last Name: {student[2]}")

def menu():
    while True:
        print("|", "=" * 27, "|")
        print("| STUDENT INFORMATION SYSTEM  |")
        print("|", "=" * 27, "|")
        print("| 1. Add Student              |")
        print("| 2. Search Student           |")
        print("| 3. View All Students        |")
        print("| 4. Edit Student             |")
        print("| 5. Delete Student           |")
        print("| 6. View Archive             |")
        print("| 7. Exit                     |")
        print("|", "=" * 27, "|")
        choice = input("Choice:")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            view_all_students()
        elif choice == '4':
            edit_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            view_archive()
        elif choice == '7':
            print("Exiting the System.")
            break
        else:
            print("\nInvalid Choice. Please Try Again.")

if __name__ == "__main__":
    menu()