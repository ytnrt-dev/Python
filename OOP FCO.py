from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str, emp_id: str, department: str, email: str):
        self.__name       = name
        self.__emp_id     = emp_id
        self.__department = department
        self.__email      = email

    # Getters

    def get_name(self) -> str:
        return self.__name

    def get_id(self) -> str:
        return self.__emp_id

    def get_department(self) -> str:
        return self.__department

    def get_email(self) -> str:
        return self.__email

    #Setters (with validation)

    def set_name(self, name: str):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = name

    def set_department(self, department: str):
        if not department.strip():
            raise ValueError("Department cannot be empty.")
        self.__department = department

    def set_email(self, email: str):
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Invalid email address.")
        self.__email = email

    # Abstract Methods (Polymorphism)

    @abstractmethod
    def calculate_salary(self) -> float:
        """Returns the calculated monthly salary."""
        pass

    @abstractmethod
    def position(self) -> str:
        """Returns the job position title."""
        pass

    #String Representation (Polymorphism)

    def __str__(self) -> str:
        return (
            f"ID: {self.get_id():<10} | "
            f"Name: {self.get_name():<20} | "
            f"Dept: {self.get_department():<15} | "
            f"Role: {self.position():<18} | "
            f"Salary: ₱{self.calculate_salary():,.2f}"
        )


# Concrete Subclasses (Inheritance + Polymorphism)

class Manager(Employee):
    """Represents a Manager with a fixed monthly salary."""

    SALARY = 10_000.0

    def calculate_salary(self) -> float:
        return self.SALARY

    def position(self) -> str:
        return "Manager"


class RegularEmp(Employee):
    """Represents a Regular Employee with a fixed monthly salary."""

    SALARY = 6_000.0

    def calculate_salary(self) -> float:
        return self.SALARY

    def position(self) -> str:
        return "Regular Employee"


class ContractEmp(Employee):
    """
    Represents a Contractual Employee paid by hourly rate.
    Salary = hourly_rate × hours_worked
    """

    def __init__(self, name: str, emp_id: str, department: str, email: str,
                hourly_rate: float, hours_worked: float):
        super().__init__(name, emp_id, department, email)
        self.__hourly_rate  = hourly_rate
        self.__hours_worked = hours_worked

    def get_hourly_rate(self) -> float:
        return self.__hourly_rate

    def get_hours_worked(self) -> float:
        return self.__hours_worked

    def set_hourly_rate(self, rate: float):
        if rate <= 0:
            raise ValueError("Hourly rate must be positive.")
        self.__hourly_rate = rate

    def set_hours_worked(self, hours: float):
        if hours < 0:
            raise ValueError("Hours worked cannot be negative.")
        self.__hours_worked = hours

    def calculate_salary(self) -> float:
        return self.__hourly_rate * self.__hours_worked

    def position(self) -> str:
        return "Contractual Employee"


# Employee Registry (Data Store)

employees: list[Employee] = []

# Employee Archived List (Data Storage)

archived_employees: list[Employee] = []

# Helper Utilities

def _find_employee(emp_id: str) -> Employee | None:
    """Return the employee matching the given ID, or None."""
    for emp in employees:
        if emp.get_id() == emp_id:
            return emp
    return None


def _id_exists(emp_id: str) -> bool:
    """Check if an employee ID already exists."""
    return _find_employee(emp_id) is not None


def _print_header(title: str):
    print("\n" + "=" * 72)
    print(f"  {title}")
    print("=" * 72)


def _print_employees(emp_list: list[Employee]):
    """Pretty-print a list of employees."""
    if not emp_list:
        print("  (no employees to display)")
        return
    for emp in emp_list:
        print(" ", emp)


# ──────────────────────────────────────────────
# CRUD Functions
# ──────────────────────────────────────────────

def add_employee():
    """Prompt the user and add a new employee to the registry."""
    print("\n--- Add Employee ---")
    try:
        name       = input("  Name       : ").strip()
        emp_id     = input("  Employee ID: ").strip()
        department = input("  Department : ").strip()
        email      = input("  Email      : ").strip()

        if not name or not emp_id or not department:
            print("Name, ID, and Department cannot be blank.")
            return

        if _id_exists(emp_id):
            print(f"Employee ID '{emp_id}' already exists.")
            return

        print("\n  Employee Type:")
        print("  1 - Manager")
        print("  2 - Regular Employee")
        print("  3 - Contractual Employee")
        choice = input("  Choose type: ").strip()

        if choice == "1":
            employee = Manager(name, emp_id, department, email)

        elif choice == "2":
            employee = RegularEmp(name, emp_id, department, email)

        elif choice == "3":
            hourly_rate  = float(input("  Hourly Rate (₱): "))
            hours_worked = float(input("  Hours Worked   : "))
            employee = ContractEmp(name, emp_id, department, email,
                                   hourly_rate, hours_worked)
        else:
            print("Invalid employee type.")
            return

        employees.append(employee)
        print(f"Employee '{name}' added successfully!")

    except ValueError as e:
        print(f"Error: {e}")


def view_employees():
    """Display all employees in a formatted table."""
    if not employees:
        print("\n  No employees on record.")
        return
    _print_header(f"EMPLOYEE LIST  ({len(employees)} record/s)")
    _print_employees(employees)
    print("=" * 72)


def update_employee():
    """Find an employee by ID and update their editable fields."""
    if not employees:
        print("\n  No employees yet.")
        return

    print("\n--- Update Employee ---")
    emp_id = input("  Enter Employee ID to update: ").strip()
    emp = _find_employee(emp_id)

    if emp is None:
        print(f"No employee found with ID '{emp_id}'.")
        return

    print(f"  Updating: {emp.get_name()} ({emp.position()})")
    print("  (Leave blank to keep current value)\n")

    try:
        name = input(f"  Name [{emp.get_name()}]: ").strip()
        if name:
            emp.set_name(name)

        dept = input(f"  Department [{emp.get_department()}]: ").strip()
        if dept:
            emp.set_department(dept)

        email = input(f"  Email [{emp.get_email()}]: ").strip()
        if email:
            emp.set_email(email)

        # Extra fields for contractual employees
        if isinstance(emp, ContractEmp):
            rate = input(f"  Hourly Rate [₱{emp.get_hourly_rate()}]: ").strip()
            if rate:
                emp.set_hourly_rate(float(rate))

            hours = input(f"  Hours Worked [{emp.get_hours_worked()}]: ").strip()
            if hours:
                emp.set_hours_worked(float(hours))

        print("Employee updated successfully!")

    except ValueError as e:
        print(f"Error: {e}")


def delete_employee():
    """Remove an employee from the registry by ID."""
    if not employees:
        print("\n  No employees yet.")
        return

    print("\n--- Delete Employee ---")
    emp_id = input("  Enter Employee ID to delete: ").strip()
    emp = _find_employee(emp_id)

    if emp is None:
        print(f"No employee found with ID '{emp_id}'.")
        return

    confirm = input(f"  Delete '{emp.get_name()}' ({emp.position()})? (y/n): ").strip().lower()
    if confirm == "y":
        employees.remove(emp)
        print(f"Employee '{emp.get_name()}' deleted.")
    else:
        print("  Deletion cancelled.")


# Search

def search_employee():
    """Search for employees by ID or name (case-insensitive)."""
    if not employees:
        print("\n  No employees yet.")
        return

    print("\n--- Search Employee ---")
    keyword = input("  Enter name or ID to search: ").strip().lower()
    results = [
        emp for emp in employees
        if keyword in emp.get_name().lower() or keyword in emp.get_id().lower()
    ]

    _print_header(f"SEARCH RESULTS FOR '{keyword}'  ({len(results)} match/es)")
    _print_employees(results)
    print("=" * 72)

# Promote
"""Will promote an employee into the next rank by ID."""
def promote_employee():
    if not employees:
        print("\n  No employees yet.")
        return

    print("\n--- Promote Employee ---")
    emp_id = input("  Enter Employee ID to promote: ").strip()
    emp = _find_employee(emp_id)

    if emp is None:
        print("Employee not found.")
        return

    if isinstance(emp, RegularEmp):
        employees.remove(emp)
        promoted = Manager(emp.get_name(), emp.get_id(), emp.get_department(), emp.get_email())
        employees.append(promoted)
        print(f"{emp.get_name()} has been promoted to Manager!")
        print(f"New Salary: ₱{promoted.calculate_salary():,.2f}")

    elif isinstance(emp, ContractEmp):
        employees.remove(emp)
        promoted = RegularEmp(emp.get_name(), emp.get_id(), emp.get_department(), emp.get_email())
        employees.append(promoted)
        print(f"{emp.get_name()} has been promoted to Regular Employee!")
        print(f"New Salary: ₱{promoted.calculate_salary():,.2f}")

    else:
        print(f"{emp.get_name()} is already a Manager.")
        print(f"Current Salary: ₱{emp.calculate_salary():,.2f}")

# Archive

def archive_employee():
    """Move an employee to the archive instead of deleting."""
    if not employees:
        print("\n  No employees yet.")
        return

    print("\n--- Archive Employee ---")
    emp_id = input("  Enter Employee ID to archive: ").strip()
    emp = _find_employee(emp_id)

    if emp is None:
        print(f"No employee found with ID '{emp_id}'.")
        return

    confirm = input(f"  Archive '{emp.get_name()}' ({emp.position()})? (y/n): ").strip().lower()
    if confirm == "y":
        employees.remove(emp)
        archived_employees.append(emp)
        print(f"Employee '{emp.get_name()}' archived successfully.")
    else:
        print("  Archiving cancelled.")

# View archived list

def view_archived_employees():
    """Display archived employees."""
    if not archived_employees:
        print("\n  No archived employees.")
        return
    _print_header(f"ARCHIVED EMPLOYEES  ({len(archived_employees)} record/s)")
    _print_employees(archived_employees)
    print("=" * 72)

# Main Menu

def display_menu():
    print("\n╔══════════════════════════════╗")
    print("║  Employee Management System  ║")
    print("╠══════════════════════════════╣")
    print("║  1 - Add Employee            ║")
    print("║  2 - View All Employees      ║")
    print("║  3 - Update Employee         ║")
    print("║  4 - Delete Employee         ║")
    print("║  5 - Search Employee         ║")
    print("║  6 - Promote Employee        ║")
    print("║  7 - Archive Employee        ║")
    print("║  8 - View Archived Employees ║")
    print("║  0 - Exit                    ║")
    print("╚══════════════════════════════╝")


def main():
    """Entry point — runs the main menu loop."""
    actions = {
        "1": add_employee,
        "2": view_employees,
        "3": update_employee,
        "4": delete_employee,
        "5": search_employee,
        "6": promote_employee,
        "7": archive_employee,
        "8": view_archived_employees,
    }

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("\nGoodbye!\n")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()