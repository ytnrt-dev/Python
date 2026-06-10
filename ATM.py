balance = 1000
choice = 0

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Choice: "))

    if choice == 1:
        print(f"Balance: ${balance}")

    elif choice == 2:
        amount = float(input("Enter deposit amount: $"))
        if amount > 0:
            balance += amount
            print(f"Deposited ${amount}. New Balance: ${balance}")
        else:
            print("Invalid amount!")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: $"))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${balance}")

    elif choice == 4:
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-4.")