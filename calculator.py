import art
import os



# Calculator Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1/n2

# Keys dictionary
operations ={
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}
#


def calculator():
    os.system('cls')
    print(art.logo)
    num1 = float(input("What's the first number: "))
    should_continue = True

    while should_continue:
        num2 = float(input("What's the next number: "))
        # Print the operation symbol
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        calculation_function = operations[operation_symbol]
        result = round(calculation_function(num1,num2), 2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result} , or type 'n' to start again ").lower() == "y":
            num1 = result
        else:
            should_continue = False
            calculator()

calculator()

# We use a recursion here, a function which is going to call itself!
# how to break out of a recursion then???