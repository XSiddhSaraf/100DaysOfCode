# Calculator app

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

num1 = int(input('What is the first number? '))

for key in operations:
    print(key)
operation_symbol = input('Pick one operation from above list.')
num2 = int(input('What is the second number? '))

calculation_function = operations[operation_symbol]

answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
