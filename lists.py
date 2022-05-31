def print_menu():
    options = ['Add', 'Remove', 'List', 'Find', 'Sort', 'Quit']
    print('OPTIONS')
    print('**************')
    print('Add')
    print('Remove')
    print('List')
    print('Find')
    print('Sort')
    print('Quit')

cities = ['Boston', 'Worcester', 'Plymouth', 'Nantucket', 'Gloucester']
choice = ''

while choice != 'quit' and choice != 'Quit':
    print_menu()
    choice = input('Enter your choice: ')
    print(choice)
    if choice == 'Add' or choice == 'add':
        add_city = input('Enter a city to add: ')
        cities.append(add_city)
        print('You have added {} to the list.'.format(add_city))
    elif choice == 'Remove' or choice == 'remove':
        temp = 'n'
        while temp == 'n':
            rem_city = input('Enter a city to remove: ')
            if rem_city not in cities:
                print('The city you entered was not in the list.')
            else:
                cities.remove(rem_city)
                print('You have removed {} from the list.'.format(rem_city))
                temp = 'y'
    elif choice == 'List' or choice == 'list':
        print(' '.join(cities))
    elif choice == 'Find' or choice == 'find':
        temp = 'n'
        while temp == 'n':
            find_city = input('Enter a city to get the index number: ')
            if find_city not in cities:
                print('The city you entered was not in the list.')
            else:
                index = cities.index(find_city)
                print('{} is in index {}.'.format(find_city, index))
                temp = 'y'
    elif choice == 'Sort' or choice == 'sort':
        cities.sort()
        print(cities)
print('Exiting...')