# Sets an empty string for people's weights.
people_weights = []

# Declares how many weights will be taken in
num_weights = 4

# Declares the orginal number weight, only used for the string of asking for a weight.
nw = 1

# Loops through the range of num_weights and takes in all the user entered weights, appends them into the empty list.
for i in range(num_weights):
    weight_input = float(input('Enter weight {}:'.format(nw)))
    nw += 1
    people_weights.append(weight_input)
    print()

# Prints the user's entered weights.
print('Weights: {}'.format(people_weights))
print()

# Gets sum of all weights in the list.
sum_weights = sum(people_weights)

# Calculates the average weight.
avg_weights = sum_weights / num_weights

# Prints the average weight.
print('Average weight: {}'.format(avg_weights)) 

# Chooses the highest value in the list, the 'max' weight.
max_weight = max(people_weights)

# Prints the max weight.
print('Max weight: {:.2f}\n'.format(max_weight))

# Asks the user for an input to find a weight with index numbers.
user_location = int(input('Enter a list location (1 - 4):'))
print()

# Subtracts the user's input because the index starts at 0.
user_index = user_location - 1

# Sets the user's indexed weight to a variable.
num_user_selected = people_weights[user_index]

# Function that converts pounds to kilos.
def pounds_to_kilo(weight):
    kilo = weight / 2.2
    return kilo

# Sets the index pound to kilos.
user_kilo = pounds_to_kilo(num_user_selected)

# Prints the user's weights in pounds and kilograms.
print('Weight in pounds: {:.2f}'.format(num_user_selected))
print('Weight in kilograms: {:.2f}'.format(user_kilo))
print()

# Sorts the list.
people_weights.sort()

# Prints the sorted list.
print('Sorted list: {}'.format(people_weights))