#! python3
#rock paper scissors

import random

def gameLogic(player1Choice, player2Choice):
    if player1Choice == player2Choice:
        return 0

    playerNextIndex = (player1Choice + 1) % 3
    
    winner = 2 if playerNextIndex == player2Choice else 1
    
    return winner


RPS = ['rock', 'paper', 'scissors']
maxGames = 3
computerScore = 0
playerScore = 0
gameCount = 0

print('I challenge you to rock paper scissors, best 2 out of 3!')

while gameCount < maxGames:    #loops for 3 rounds
    playerChoice = input('rock paper scissors! Make your choice:')
    try:
        playerChoiceIndex = RPS.index(playerChoice)
    except (ValueError):
        print('Are you serious? The game is called "rock, paper, scissors"! Maybe try picking one of those, hmmmmmmm?')
        continue

    computerChoiceIndex = random.randint(0, 2)
    computerChoice = RPS[computerChoiceIndex]
    print(computerChoice)
    winner = gameLogic(playerChoiceIndex, computerChoiceIndex)

    if winner == 0:
        print('It\'s a tie!')
    else:
        if winner == 2:
            computerScore += 1
            print('{0} beats {1}, you are a little bitch tit'.format(computerChoice, playerChoice))
        else:
            playerScore += 1
            print('apparently you win this time')
        gameCount += 1

print('I won {} games and you won {}'.format(computerScore, playerScore))

if computerScore > playerScore:
    print('I beat you peasant, worship my awesomeness')
else:
    print('You beat me but you still suck at life and cant code for shit...')

#im less a wizard and more of a hack
