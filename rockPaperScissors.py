#! python3
#rock paper scissors

""" Im sure that I still have some absolute failures in my formatting
that are clearly written out in pep 8 but I will figure that out
eventually
"""

import random

class rps_game():
    
    # Initilize the players
    def __init__(self, score, selection, index):
        self.score = score
        self.selection = selection
        self.index = index

    # Method to change score
    def score_increase(self):
        self.score += 1
        return self.score
    
    # Method for choice
    def make_choice(self):
        self.selection = input('rock, paper scissors! Make your choice... ')
        return self.selection
    
    # Method for indexing
    def choice_index(self, selection):
        self.index = RPS.index(self.selection)
        return self.index

# Determines which player wins based on an index of their choice   
def game_logic(player_1_choice, player_2_choice):
    if player_1_choice == player_2_choice:
        return 0

    player_next_index = (player_1_choice + 1) % 3
    
    winner = 2 if player_next_index == player_2_choice else 1
    
    return winner

# Setting global variables and initializing the players
RPS = ['rock', 'paper', 'scissors']
max_games = 3
player = rps_game(0, '', '')
computer = rps_game(0, '', '')
game_count = 0

# Main body of game
print('I challenge you to rock paper scissors, best 2 out of 3!')

while game_count < max_games:    #loops for 3 rounds
    player.make_choice()
    try:
        player.choice_index(player.selection)
    except (ValueError):
        print('Fool, its rock paper scissors. Those are your only choices!')
        continue
        
    computer.selection = random.choice(RPS)
    computer.choice_index(computer.selection)
    
    print(computer.selection)
    winner = game_logic(player.index, computer.index)

    if winner == 0:
        print('It\'s a tie!')
    else:
        if winner == 2:
            computer.score_increase()
            print('{0} beats {1}, you are a little bitch tit'
                  .format(computer.selection, player.selection))
        else:
            player.score_increase()
            print('apparently you win this time')
        game_count += 1

    #breaks if a player wins two games
    if player.score or computer.score == 2:
        break

print('I won {} games and you won {}'.format(computer.score, player.score))

if computer.score > player.score:
    print('I beat you peasant, worship my awesomeness')
else:
    print('You beat me but you still suck at life and cant code for shit...')

# I'm less a wizard with a little class
