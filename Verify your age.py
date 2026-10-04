print("Welcome, please verify your age first.")

age = 0
while age < 18:
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            print("\nYou must be 18 years old or above to enter.")
        elif age >= 18:
            print("\nAge verified, please sign up.")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")
        
username = input("Enter username: ")
password = input("Enter password: ")
print("\nRegistration successful! Now, please sign in.")

while True:
    login_username = input("Enter username: ")
    login_password = input("Enter password: ")
    
    if login_username == login_username and login_password == login_password:
        print("\nLogin successful! Welcome back", login_username + "!")
        break
    else:
        print("\nLogin failed. Incorrect username or password. Try again.")