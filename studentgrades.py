# Gets user input
usr_list = []
usr_input = input('Enter the number grades seperated by a comma: ')
usr_list = usr_input.split(',')

# Converts list to integers
for i in range(0, len(usr_list)):
    usr_list[i] = int(usr_list[i])

# Checks if all numbers are less than 101 and greater than -1
check1 = all(i >= 0 for i in usr_list)
check2 = all(i <= 100 for i in usr_list)

# Sorts list and removes lowest number
usr_list.sort()
usr_list.pop(0)

# Calcualtes sum and average
sum = sum(usr_list)
average = sum / len(usr_list)

# Converts grades to a letter and prints the average grade
if check1 == 'false' and check2 == 'false':
    print('You have entered numbers that may be incorrect.')
elif average >= 90 and average <= 100:
    print('A')
elif average >= 80 and average <= 89:
    print('B')
elif average >= 70 and average <= 79:
    print('C')
elif average >= 60 and average <= 69:
    print('D')
else:
    print('F')

