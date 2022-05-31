import random

# INITIAL VARIABLES
choices = ['rock', 'paper', 'scissors']
user_score = 0
pc_score = 0

# rock beats scissors
# paper beats rock
# scissors beats paper

while user_score < 5 or pc_score < 5:
    pc_choice = random.choice(choices)
    user_choice = input('Enter a choice (rock, paper or scissors): ')
    msg = 'You chose ' + user_choice + '. Computer chose ' + pc_choice + '.'
    
    #INVALID CHOICE
    if user_choice not in choices:
        print('Invalid Choice')
        continue
    
    #TIE
    elif user_choice == pc_choice:
        print(msg)
        print('User and PC has tied.')
        continue
    
    #USER WINS
    elif user_choice == 'rock' and pc_choice == 'scissors':
        print(msg)
        print('User has won.')
        user_score += 1
        continue
    elif user_choice == 'paper' and pc_choice == 'rock':
        print(msg)
        print('User has won.')
        user_score += 1
        continue
    elif user_choice == 'scissors' and pc_choice == 'paper':
        print(msg)
        print('User has won.')
        user_score += 1
        continue

    #PC WINS
    elif pc_choice == 'rock' and user_choice == 'scissors':
        print(msg)
        print('PC has won.')
        pc_score += 1
        continue
    elif pc_choice == 'paper' and user_choice == 'rock':
        print(msg)
        print('PC has won.')
        pc_score += 1
        continue
    elif pc_choice == 'scissors' and user_choice == 'paper':
        print(msg)
        print('PC has won.')
        pc_score += 1
        continue

#WIN MESSAGES
if pc_score == 5:
    print('The computer has won the game.')
elif user_score == 5:
    print('The user has won the game.')