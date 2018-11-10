#! python3
#rock paper scissors

import random


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

#im basically a wizard
            


