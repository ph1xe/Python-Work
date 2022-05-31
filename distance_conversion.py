
# welcome message function
def display_welcome():
    print("Feet and Meters Converter")
    print()

# display menu function
def display_menu(): 
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

    display_welcome()

again = 'y'

while again == 'y':
    display_menu()
    choice = input('Select a conversion (a or b): ')
    print()
    if choice == 'a':
        feetinp = int(input('Enter the amount of feet: '))
        fttometer = feetinp * 0.3048
        print('{:.2f} meters.'.format(fttometer))
    elif choice == 'b':
        meterinp = int(input('Enter the amount of meters: '))
        metertoft = meterinp / 0.3048
        print('{:.2f} feet.'.format(metertoft))
    else:
        print('Invalid Choice')
    again = input('Would you like another conversion? (y or n): ')
    print()

print('Program is finished.')