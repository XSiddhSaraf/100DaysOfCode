# Calculator app
from art1 import calculator_logo
# Add


def add(n1, n2):
    return n1 + n2

# Substract


def sub(n1, n2):
    return n1 - n2

# Multiplication


def mul(n1, n2):
    return n1 * n2

# Division


def div(n1, n2):
    return n1 / n2


operations = {'+': add, '-': sub, '*': mul, '/': div}


def calculator():
    print(calculator_logo)
    num1 = int(input('What is the first number? '))

    for key in operations:
        print(key)

    should_continue = True

    while should_continue:
        operation_symbol = input('Pick one operation ')
        num2 = int(input('What is the next number? '))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type y to continue with the {answer} or n to start a new calculation ") == 'y':
            num1 = answer

        else:
            should_continue = False
            calculator()


calculator()
