import random

def roll():
    value = random.randint(1, 6)
    return value

print('Dice Roller')
print('')
rdice = input('Roll the dice? (y/n): ')
while rdice == 'y':
    dice1 = roll()
    dice2 = roll()
    total = dice1 + dice2
    print('Dice 1:', dice1)
    print('Dice 2:', dice2)
    print('Total:', total)
    if dice1 == 1 and dice2 == 1:
        print('Snake eyes!')
    elif dice1 == 6 and dice2 == 6:
        print('Boxcars!')
    rdice = input('Roll the dice? (y/n): ')
