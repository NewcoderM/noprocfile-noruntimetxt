import tkinter as tk

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter numeric values.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
tk.Label(root, text="First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Create a dropdown menu for operations
operation_var = tk.StringVar(root)
operation_var.set("Add")  # default value
operations_menu = tk.OptionMenu(root, operation_var, "Add", "Subtract", "Multiply", "Divide")
operations_menu.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the application
root.mainloop()
