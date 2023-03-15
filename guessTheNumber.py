# Guess the number game
import random
mysteryNumber = random.randint(1, 30)
print('I am thinking of a number between 1 and 30')

# Ask the player to guess 7 times

for guessesTaken in range(1,8):
    print('Take a guess.')
    guess = int(input())

    if guess < mysteryNumber:
        print('Too low!')
    elif guess > mysteryNumber:
        print('Too high!')
    else:
        break

if guess == mysteryNumber:
    print('You are a magician! You guessed the number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Sorry. The number I was thinking of was ' + str(mysteryNumber))
