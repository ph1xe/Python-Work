from calendar import day_abbr
import datetime

# Print the current date and time.
now = datetime.datetime.now()
print('Current date and time: {}'.format(now))
print()

# Print the current date.
td = datetime.date.today()
print('Current date: {}'.format(td))
print()

# Print the current date.
print('Date: {}'.format(datetime.date.today()))
print()

# Prints the current month, day and year.
month = td.month
day = td.day
year = td.year

print('Month: {}'.format(month))
print('Day: {}'.format(day))
print('Year: {}'.format(year))
print()

# Days until my birthday
birth_date = datetime.date(year = 2022, month = 10, day = 26)
current_date = datetime.date.today()
t3 = birth_date - current_date
print("Days until my birthday (October 26): ", t3)