#! python3
#rock paper scissors

import random

<<<<<<< HEAD
=======
def gameLogic(player, computer, playerScore, computerScore):
    playerIndex = RPS.index(player)
    computerIndex = RPS.index(computer)

    gameIncrement = 0
    if (playerIndex != computerIndex):
        gameIncrement = 1
        playerNextIndex = (playerIndex + 1) % len(RPS)
        
        if (playerNextIndex == computerIndex):
            computerScore += 1
        else:
            playerScore += 1

    return gameIncrement, playerScore, computerScore
>>>>>>> 795877261138d3255d3b42d52da3fd811edad5f8

maxGames=3
RPS=['rock','paper','scissors']     

computerScore=0   
playerScore=0  
gameCount=0   
print('I challenge you to rock paper scissors, best 2 out of 3!')
while gameCount < maxGames:    #loops for 3 rounds
    print('rock paper scissors!')
    player=input()
    computer=random.choice(RPS)
    print(computer)
<<<<<<< HEAD
    if player==computer:
        print('its a tie!')
        gameCount -= 1   #makes sure there can be no tie at the end

    #sets the rules of rock paper scissors and tracks wins    
    elif player == 'rock':
        if computer == 'paper':
            print('I win!')
            computerScore += 1
        elif computer == 'scissors':
            print('You win')
            playerScore += 1
    elif player == 'paper':
        if computer == 'rock':
            print('you win')
            playerScore += 1
        elif computer == 'scissors':
            print('I win!')
            computerScore += 1
    elif player == 'scissors':
        if computer == 'rock':
            print('I win!')
            computerScore += 1
        elif computer == 'paper':
            print('you win')
            playerScore += 1
            
    gameCount+=1
    #if playerScore or computerScore == 2: 
         #break
        #still doesnt fucking work...
    
print('I won {} games, and you won {} games'.format(computerScore, playerScore))
if computerScore > playerScore:
    print('I beat you!')
else:
    print('You are clearly very good at this game')
=======
    gameIncrement, newComputerScore, newPlayerScore = gameLogic(computer, player, computerScore, playerScore)
>>>>>>> 795877261138d3255d3b42d52da3fd811edad5f8

    if gameIncrement == 0:
        print('It\'s a tie!')
    else:
        if newComputerScore > computerScore:
            print('{0} beats {1}, you are a little bitch tit'.format(computer, player))
        else:
            print('apparently you win this time')
    computerScore = newComputerScore
    playerScore = newPlayerScore
    gameCount += gameIncrement

print('I won {} games and you won {}'.format(computerScore, playerScore))
if computerScore > playerScore:
    print('I beat you peasant, worship my awesomeness')
else:
    print('You beat me but you still suck at life and cant code for shit...')

#im less a wizard and more of a hack
