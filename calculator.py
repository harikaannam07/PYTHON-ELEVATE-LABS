# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def show_menu():
    print("\n Select Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def main():
    print(" Welcome to the Python CLI Calculator!")

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print(" Exiting calculator. Thank you!")
            break

        if choice not in ['1', '2', '3', '4']:
            print(" Invalid choice. Please select from 1 to 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(" Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print(f" Result: {result}")

if __name__ == "__main__":
    main()
