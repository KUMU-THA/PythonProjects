def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y."""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    """Get a valid number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "Division"

            print(f"\nOperation: {operation}")
            print(f"First Number: {num1}")
            print(f"Second Number: {num2}")
            print(f"Result: {result}\n")
        
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
