# calculator.py
import logging
import database

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError
    return x / y

def calculate():
    print("Enter the first number:")
    num1 = float(input())
    print("Enter the operator (+, -, *, /):")
    operator = input()
    print("Enter the second number:")
    num2 = float(input())
    try:
        if operator == "+":
            result = add(num1, num2)
        elif operator == "-":
            result = subtract(num1, num2)
        elif operator == "*":
            result = multiply(num1, num2)
        elif operator == "/":
            result = divide(num1, num2)
        else:
            raise Exception("Invalid operator")
        print("Result:", result)
        log_operation(f"{num1} {operator} {num2}", result)
        database.save_calculation(f"{num1} {operator} {num2}", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Error: Invalid expression ({e})")

def log_operation(expression, result):
    logging.basicConfig(filename='operations.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    log_entry = f"Expression: {expression}, Result: {result}"
    logging.info(log_entry)
    print("Operation logged successfully.")