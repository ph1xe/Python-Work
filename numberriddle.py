again = 'y'

while again == 'y':
    number = int(input('Enter an integer: '))
    print('User entered', number)
    doubled = number * 2
    print('Number doubled is', doubled)
    plus6 = doubled + 6
    print('Number doubled plus 6 is', plus6)
    div2 = plus6 / 2
    print('Divided by 2 is', div2)
    min = div2 - number
    print('And then minus the original is', min)
    print()
    again = input('Try again? y or n: ')