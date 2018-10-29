#! python3
#rock paper scissors

import random

RPS=['rock','paper','scissors']     #list of choices

I=0   #computer score
You=0  #player score
game=0   #keeps track of game number
print('I challenge you to rock paper scissors, best 2 out of 3!')
while game<=2:    #loops for 3 rounds
    print('rock paper scissors!')
    player=input()
    computer=random.choice(RPS)
    print(computer)
    if player==computer:
        print('its a tie!')
        game-=1   #makes sure there can be no tie at the end

    #sets the rules of rock paper scissors and tracks wins    
    elif player=='rock':
        if computer=='paper':
            print('I win!')
            I+=1
        elif computer=='scissors':
            print('You win')
            You+=1
    elif player=='paper':
        if computer=='rock':
            print('you win')
            You+=1
        elif computer=='scissors':
            print('I win!')
            I+=1
    elif player=='scissors':
        if computer=='rock':
            print('I win!')
            I+=1
        elif computer=='paper':
            print('you win')
            You+=1
            
    game+=1
print('I won '+str(I)+' games, and you won '+str(You)+' games')
if I>You:
    print('I beat you!')
else:
    print('You are clearly very good at this game')

#im basically a wizard
            


