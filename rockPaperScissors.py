#! python3
#rock paper scissors

import random

class gameState():
    score = 0
    choice = ''
    index = ''
    
def gameLogic(player1Choice, player2Choice):
    if player1Choice == player2Choice:
        return 0

    playerNextIndex = (player1Choice + 1) % 3
    
    winner = 2 if playerNextIndex == player2Choice else 1
    
    return winner


RPS = ['rock', 'paper', 'scissors']
maxGames = 3
player = gameState()
computer = gameState()
gameCount = 0

print('I challenge you to rock paper scissors, best 2 out of 3!')

while gameCount < maxGames:    #loops for 3 rounds
    player.choice = input('rock paper scissors! Make your choice:')
    try:
        player.index = RPS.index(player.choice)
    except (ValueError):
        print('Are you serious? The game is called "rock, paper, scissors"! Maybe try picking one of those, hmmmmmmm?')
        continue

    computer.index = random.randint(0, 2)
    computer.choice = RPS[computer.index]
    print(computer.choice)
    winner = gameLogic(player.index, computer.index)

    if winner == 0:
        print('It\'s a tie!')
    else:
        if winner == 2:
            computer.score += 1
            print('{0} beats {1}, you are a little bitch tit'
                  .format(computer.choice, player.choice))
        else:
            player.score += 1
            print('apparently you win this time')
        gameCount += 1

print('I won {} games and you won {}'.format(computer.score, player.score))

if computer.score > player.score:
    print('I beat you peasant, worship my awesomeness')
else:
    print('You beat me but you still suck at life and cant code for shit...')

#im less a wizard and more of a hack
