again = 'y'

print('Change Calculator')

while again == 'y' or again == 'Y':
    amount = int(input('Enter amount of cents (0-99): '))
    if amount<=0:
        print("No change")
    else:
        dollar = int(amount/100)
        amount = amount % 100
        quarter = int(amount/25)
        amount = amount % 25
        dime = int(amount/10)
        amount = amount % 10
        nickel = int(amount/5)
        penny = amount % 5

        if dollar >= 1:
            print("Dollars: " + str(dollar))
        if quarter >= 1:
            print("Quarters: " + str(quarter))
        if dime >= 1:
            print("Dimes: " + str(dime))
        if nickel >= 1:
            print("Nickels: " + str(nickel))
        if penny >= 1:
            print("Pennies: " + str(penny))
    again = input('Continue? (y/n): ')

print('Bye!')