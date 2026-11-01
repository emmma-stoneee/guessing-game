from analyticskit import *
import random
secret_number= random.randint(1,10)

while True:
    secret_number= random.randint(1,10)
    guess = single_input('Guess a number between 1 and 10', mask=False)
    guess= int(guess)

    if guess == secret_number:
        show_message('You win!', 'You guessed the correct number.')
        
    else:
        show_message(f'You lose', f'The correct number was {secret_number}.')


    playagain = single_input('Would you like to play again? Enter y/n.', mask=False)

    if playagain.lower() != 'y':
        break