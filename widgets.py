import time
import datetime

menu_options = ['Set a timer', 'Get the date.', 'Exit']

def menu():
    '''Displays the menu.'''
    print('***Widget Apps***')
    num = 1
    for i in menu_options:
        print('({}) {}'.format(num, i))
        num += 1
    print()

def loop_choices():
    '''Loops the user's choices until they choose exit.'''
    loop = True
    while loop == True:
        menu()
        time.sleep(1)
        usr_choice = int(input('Please select your choice (1-{}): '.format(len(menu_options))))
        if int(usr_choice) > len(menu_options) or int(usr_choice) < 1:
            print('You have selected an invalid option. Returning you to the menu.')
            print()
        elif usr_choice == 1:
            timer()
        elif usr_choice == 2:
            date()
        elif usr_choice == 3:
            loop = False
            goodbye()
            

def timer():
    '''Gets the user input in seconds and does a countdown with user's selected time.'''
    print('**Opening Timer**')
    time.sleep(2)
    
    # Gets the user selection.
    countdown = input('Enter the time you would like (in seconds): ')
    original_time = countdown

    # Lets the user know the time they selected and that the timer has started.
    print('You have selected a {} second timer.'.format(countdown))
    time.sleep(1)
    print('Starting timer.')

    # Prints the countdown.
    for i in range(int(countdown)):
        print(str(countdown))
        time.sleep(1)
        countdown = int(countdown)
        countdown -= 1

    # Lets the user know the timer has been completed.
    print('{} second timer has been completed. Returning you to the main menu.'.format(original_time))
    print()

def date():
    '''Dispalys the current date and time.'''
    print('**Opening Calendar**')
    time.sleep(2)
    today = datetime.datetime.now()
    
    # Prints the current date and time.
    print('**Current date and time**')
    print(today.strftime('%m-%d-%Y at %H:%M'))
    print()

def goodbye():
    print('Thank you for using the widget apps.')

loop_choices()