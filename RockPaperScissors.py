# Classic Rock, paper, scissors game

import random, sys

print('Rock, Paper, Scissors Time!')

wins = 0
losses = 0
ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Your move: (r)ock (p)paper (s)cissors or (q)uit')
        playersMove = input()
        if playersMove == 'q':
            sys.exit()
        if playersMove == 'r' or playersMove == 'p' or playersMove == 's':
            break
        print('Type one of r, p, s, or q.')

    if playersMove == 'r':
        print('Rock versus...')
    elif playersMove == 'p':
        print('Paper versus...')
    elif playersMove == 's':
        print('Scissors versus...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computersMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        computersMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        print('Scissors')

    if playersMove == computersMove:
        print('It is a tie!')
        ties = ties + 1
    elif playersMove == 'r' and computersMove == 's':
        print('You win!')
        wins = wins + 1
    elif playersMove == 'p' and computersMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playersMove == 's' and computersMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playersMove == 'r' and computersMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playersMove == 'p' and computersMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playersMove == 's' and computersMove == 'r':
        print('You lose!')
        losses = losses + 1

