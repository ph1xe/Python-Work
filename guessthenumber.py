import random

#this line generates a random number from 1 to 100
num = random.randint(1, 100)

print("Guess the random number between 1 and 100.  See how many attempts it takes!")

#declare a variable to hold the number of attempts that it takes
guesses = 0

#prompt the user to enter a guess and store in a variable
user_guess = int(input('Enter a guess: '))

while user_guess != num:
    if user_guess > num:
        print('Too High!')
    elif user_guess < num:
        print('Too Low!')
    guesses += 1
    user_guess = int(input('Enter a guess: '))

print('You guessed the correct number {}! It took you {} tries!'.format(num, guesses))