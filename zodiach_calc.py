import math

year_born = int(input('Input your birth year: '))
remainder = (year_born - 2000) % 12

if remainder == 0:
    print('Your Zodiac sign: Dragon')
elif remainder == 1:
    print('Your Zodiac sign: Snake')
elif remainder == 2:
    print('Your Zodiac sign: Horse')
elif remainder == 3:
    print('Your Zodiac sign: Sheep')
elif remainder == 4:
    print('Your Zodiac sign: Monkey')
elif remainder == 5:
    print('Your Zodiac sign: Rooster')
elif remainder == 6:
    print('Your Zodiac sign: Dog')
elif remainder == 7:
    print('Your Zodiac sign: Pig')
elif remainder == 8:
    print('Your Zodiac sign: Rat')
elif remainder == 9:
    print('Your Zodiac sign: Ox')
elif remainder == 10:
    print('Your Zodiac sign: Tiger')
elif remainder == 11:
    print('Your Zodiac sign: Hare')