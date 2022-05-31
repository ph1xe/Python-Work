# Menu Function
def menu():
    print('[ PYTHON CALCULATOR ]')
    print('Options:')
    print('  -Add')
    print('  -Subtract')
    print('  -Multiply')
    print('  -Divide')
    print('  -Quit')
    print('')

# Arithmetic Functions
def add(x, y):
    sum = x + y
    return sum

def subtract(x, y):
    difference = x - y
    return difference

def multiplication(x, y):
    product = x * y
    return product

def division(x, y):
    quotient = x / y
    return quotient

# Code
cont = 'y'

while cont == 'y':
    menu()
    selection = input('Enter your selection: ')
    print('You have selected', str(selection) + '.')
    if selection.lower() == 'quit':
        break
    elif selection != 'add' and selection != 'Add' and selection != 'subtract' and selection != 'Subtract' and selection != 'multiply' and selection != 'Multiply' and selection != 'Divide' and selection != 'divide':
        print('You have encountered an error, please try again.')
        continue
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    print('You have entered', num1, 'and', num2)

    if selection == 'add' or selection == 'Add':
        answer = add(num1, num2)
        print('The sum is', answer)
    elif selection == 'subract' or selection == 'Subtract':
        answer = subtract(num1, num2)
        print('The difference is', answer)
    elif selection == 'multiply' or selection == 'Multiply':
        answer = multiplication(num1, num2)
        print('The product is', answer)
    elif selection == 'divide' or selection == 'Divide':
        answer = division(num1, num2)
        print('The quotient is', answer)
    cont = input('Would you like to do another operation? (y or n): ')

print('Bye!')