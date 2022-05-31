input_month = input('Input the month (e.g. January, February etc.): ')
input_day = int(input('Input the day: '))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
if input_month in months:
    if (input_month == 'March' and input_day >= 20 and input_day <= 31) or input_month == 'April' and input_day >= 1 or input_month == 'May' and input_day >= 1 or input_month == 'June' and input_day >= 1 and input_day <= 20:
        print('Season is SPRING')
    elif input_month == 'June' and input_day >= 21 and input_day <= 30 or input_month == 'July' and input_day >= 1 or input_month == 'August' and input_day >= 1 or input_month == 'September' and input_day >= 1 and input_day <= 21:
        print('Season is SUMMER')
    elif input_month == 'September' and input_day >= 22 and input_day <= 30 or input_month == 'October' and input_day >= 1 or input_month == 'November' and input_day >= 1 or input_month == 'December' and input_day >= 1 and input_day <= 20:
        print('Season is AUTUMN')
    elif input_month == 'December' and input_day >= 21 and input_day <= 31 or input_month == 'January' and input_day >= 1 or input_month == 'February' and input_day >= 1 and input_day <= 29 or input_month == 'March' and input_day >= 1 and input_day <= 19:
        print('Season is WINTER')
    else:
        print('Invalid')
else:
    print('Invalid')