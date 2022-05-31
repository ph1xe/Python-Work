# List of Options
options = ('Display all contacts', 'Add a new contact', 'Find a phone number', 'Edit a phone number', 'Delete a contact', 'Delete All contacts', 'Exit')


def print_menu():
    '''Print the menu and promt the user'''
    
    # Prints the Title
    print('Welcome to P&W Contact Book. Valid P&W Contact Book commands are: 1-7.')
    
    # Prints the options 1-7
    num = 1
    for i in options:
        print('{}. {}'.format(num, i))
        num += 1
    
    # Temporary value to hold the loop
    temp = False
    while temp == False:
        # Asks for the user's choice
        user_choice = int(input('Enter your choice: '))

        # If user's choice is not valid, continue to the beginning of the loop
        if user_choice < 1 or user_choice > 7:
            print('The choice was invalid. Please try again.')
            continue
        
        # Breaks the loop
        else:
            temp = True
    
    # Returns the user's selection
    return user_choice

def init_phonebook():
    '''Defines the dictionary, loops through all the user's selections and runs them, prints the menu'''
    # Sets the list for the first time (EMPTY)
    phonebook = {}
    temp = False

    # Loops through user's 
    while temp == False:
        # Promts the user for an option
        choice = print_menu()

        # If the user choses 1, list the contacts
        if choice == 1:
            list_contacts(phonebook)
        
        # If the user choses 2, add the user's specified contacts to the list
        elif choice == 2:
            add_contacts(phonebook)

        # If the user choses 3, search for the user's inputted number
        elif choice == 3:
            find_contact(phonebook)

        # If the user choses 4, edit the user's contact number
        elif choice == 4:
            edit_contact(phonebook)

        # If the user choses 5, delete the user's specified contact
        elif choice == 5:
            delete_contact(phonebook)

        # If the user choses 6, delete all of the user's contacts
        elif choice == 6:
            delete_all(phonebook)

        # If the user choses 7, End the loop, send a goodbye message
        elif choice == 7:
            thanks()
            temp = True

def list_contacts(phonebook):  
    '''Prints all the keys and values of the dictionary'''

    # Checks if the list is empty
    if len(phonebook) == 0:
        print('Your Phonebook is Empty')
    
    # Iterates through the list and printing each key and value
    else:
        print('Your Phonebook is shown below:')
        for k, v in phonebook.items():
            print('{} --> {}'.format(k ,v))
    
    print()

def add_contacts(phonebook):
    '''Adds a specified name and number to the dictionary'''

    # Asks the user for a new name and number to add the dictionary
    new_num = input('Please Enter a number: ')
    new_name = input('What would you like to save the name as?: ')
    
    # Checks if the name is already in the dictionary
    if new_name in phonebook:
        print('That contact already exists in your Phonebook.')
    
    # Otherwise, adds the new key and value to the dictionary
    else:
        phonebook[new_name] = new_num
        
        # Prints the new and updated list
        print('Contact successfully saved\nYour updated phonebook is as shown below:')
        for k, v in phonebook.items():
            print('{} --> {}'.format(k ,v))
        
    print()

def find_contact(phonebook):
    '''Searches for a contact name and outputs their number'''

    # Asks to user for a name to locate
    name_to_locate = input('Enter the name of the contact details you wish to view: ')
    
    # If name is in the dictionary
    if name_to_locate in phonebook:
        print('Found {}'.format(name_to_locate))
        
        #Print name: number
        print('{}:'.format(name_to_locate), phonebook.get(name_to_locate))
    
    # If the name is not in the dictionary
    else:
        print('That contact does not exist! Returning to main menu.')
    print()

def edit_contact(phonebook):
    '''Edits the number of a specified contact'''

    # Ask the user for the name they wish to edit
    name_to_edit = input('Enter the name of the contact you wish to update: ')

    if name_to_edit in phonebook:
        print('Found {}'.format(name_to_edit))
        # Ask the user for a new number
        new_phone_number = input('Enter the new phone number for {}: '.format(name_to_edit))
        
        # Change the value for the specified key
        phonebook[name_to_edit] = new_phone_number

        # Show the updated phonebook
        print('Your Updated Phonebook is shown below:')
        for k, v in phonebook.items():
            print('{} --> {}'.format(k ,v))
    
    # If the name is not in the dictionary
    else:
        print('That contact does not exist! Returning to main menu.')   

    print()

def delete_contact(phonebook):
    '''Deletes the keys and values of a specified contact'''

    # Ask the user for a contact to delete
    name_to_del = input('Enter the name of the contact you wish to delete: ')

    if name_to_del in phonebook:
        print('Found {}'.format(name_to_del))

        # Confirm the user wants to delete the contact
        confirmation = input('Are you sure you wish to delete this contact? Yes/No: ')
        
        # If yes, delete the contact
        if confirmation.upper() == 'YES':
            # Deletes the contact
            del phonebook[name_to_del]
            
            # Shows the updated contact list
            print('Your updated phonebook is as shown below:')
            for k, v in phonebook.items():
                print('{} --> {}'.format(k ,v))
        
        # If no, returns the user to the menu
        else:
            print('You have oppted out of deleting the contacts. Returning to main menu.')

    # If the name is not in the dictionary
    else:
         print('That contact does not exist! Returning to main menu.')  
    
    print()

def delete_all(phonebook):
    '''Deletes all the keys and values from the dictionary'''

    # Get the users confirmation input
    confirmation = input('Are you sure you wish to delete all contacts? Yes/No: ')

    # If yes, clear their phonebook
    if confirmation.upper() == 'YES':
        
        # Clears phonebook
        phonebook.clear()
        print('Your phonebook is now empty.')
    
    # If no, returns the user to the menu
    else:
        print('You have opted out of deleting the contacts. Returning to main menu.')

    print()

def thanks():
    '''Thanks the user for using the phonebook'''
    
    #Goodbye message
    print('Thank you for using the P&W Contact Book. Goodbye.')

# Runs the menu and loop
init_phonebook()