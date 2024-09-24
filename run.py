def add(x, y):
    """
    Return the sum of x and y.
    Parameters:
    x (float): The first number.
    y (float): The second number.
    Returns:
    float: The sum of x and y.
    """
    return x + y


def subtract(x, y):
    """
    Return the difference of x and y.
    Parameters:
    x (float): The first number.
    y (float): The second number.
    Returns:
    float: The difference between x and y.
    """
    return x - y


def multiply(x, y):
    """
    Return the product of x and y.
    Parameters:
    x (float): The first number.
    y (float): The second number.
    Returns:
    float: The product of x and y.
    """
    return x * y


def divide(x, y):
    """
    Return the division of x by y. Handle division by zero.
    Parameters:
    x (float): The numerator.
    y (float): The denominator.
    Returns:
    float or str: The result of division, or an error message if y is zero.
    """
    if y == 0:
        return "Error! Division by zero is undefined."
    return x / y


def get_float_input(prompt):
    """
    Get a float input from the user, ensuring valid numeric input.
    Parameters:
    prompt (str): The input prompt for the user.
    Returns:
    float: A valid float number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")


def get_operation_choice():
    """
    Get a valid operation choice from the user.
    Returns:
    str: A valid operation choice from ['1', '2', '3', '4'].
    """
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("Invalid choice! Please select a valid operation (1/2/3/4).")


def perform_calculation():
    """
    Perform a calculation based on the user's choice of operation.
    """
    # Get user's choice of operation
    choice = get_operation_choice()
    # Get two numbers from the user
    num1 = get_float_input("Enter first number: ")
    num2 = get_float_input("Enter second number: ")
    # Perform the selected operation and print the result
    if choice == '1':
        result = add(num1, num2)
        operation = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        operation = "*"
    elif choice == '4':
        result = divide(num1, num2)
        operation = "/"
    print(f"\nResult: {num1} {operation} {num2} = {result}")


def confirm_continue():
    """
    Ask the user whether they want to perform another calculation.
    Returns:
    bool: True if the user wants to continue, False otherwise.
    """
    while True:
        next_calculation = input("\nContinue? (yes/no): ").strip().lower()
        if next_calculation in ['yes', 'y']:
            return True
        elif next_calculation in ['no', 'n']:
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


def calculator():
    """
    Main calculator function that allows users to perform arithmeticoperations.
    This function will continue to prompt the user for operations
    and numbers until they decide to stop. The user can perform addition,
    subtraction, multiplication, and division.
    """
    print("Welcome to the Simple Calculator!")
    while True:
        perform_calculation()
        # Ask if the user wants to continue
        if not confirm_continue():
            print("\nThank you for using the calculator. Goodbye!")
            break


if __name__ == "__main__":
    calculator()
    
