choice = ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Modulo', 'Exponent', 'Exit']

while choice != 'Exit':
    user_choice = input('What operation would you like to perform? (Addition, Subtraction, Multiplication, Division, Modulo, Exponent or Exit): ')
    
    # Invalid Choice
    if user_choice not in choice:
        print('Invalid Selection. Please input another one.')
        continue
    # Exit
    elif user_choice == 'Exit':
        print('Goodbye!')
        break
    # Valid Selections
    else:
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        if user_choice == 'Addition':
            print(num1 + num2)
        elif user_choice == 'Subtraction':
            print(num1 - num2)
        elif user_choice == 'Multiplication':
            print(num1 * num2)
        elif user_choice == 'Division':
            print(num1 / num2)
        elif user_choice == 'Modulo':
            print(num1 % num2)
        elif user_choice == 'Exponent':
            print(num1 ** num2)
        contin = input('Would you like to go again? (Y or N): ')
        if contin == 'y' or contin == 'Y':
            continue
        else:
            print('Goodbye!')
            break

