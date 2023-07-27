from replit import clear
from art import logo

def add(num1, num2):
    return num1 + num2

def subtract( num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

def calculator():
    print (logo)
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        second_number = float(input("What's the next number?: ")) 
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1=first_number, num2=second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        if input(f"Type 'y' to continue  calculating with {answer}, or type 'n' to start a new calcul;ation: ") == "y":
            first_number = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()
