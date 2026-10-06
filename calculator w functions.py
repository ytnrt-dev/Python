def calculate(num1, num2, operation):
    
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by Zero!"
    elif operation == 5:
        return num1 ** num2
    else:
        return "Error! Enter valid number."
    
def main():
    try:
        num1 = int(input("Enter the first number:"))
        
        print("\nChoose operation:" \
        "\n1. Addition" \
        "\n2. Subtraction" \
        "\n3. Multiplication" \
        "\n4. Division" \
        "\n5. Power")
        operation = int(input("Enter operation: "))

        num2 = int(input("\nEnter the second number:"))
        
        result = calculate(num1, num2, operation)
        print(f"\nResult: {result}")
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for numbers.")
if __name__ == "__main__":
    main()