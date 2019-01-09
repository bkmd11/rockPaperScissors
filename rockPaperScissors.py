#! python3
#rock paper scissors

""" Still need to play around with changing the game score
with my fancy shmancy class thingy...
Might not actually need that as a method though, works as is.
Also need to re add try/except stuff to check for a valid choice
And eventually break the game early in the event of 2 wins
but the wife is getting all worked up.


Oh and I should eliminate my use of 'choice' because its part of the random function
and that causes confusion...

plus read pep8 for formating
"""
import random

class rps_game():
    
    # Initilize the players
    def __init__(self, score, choice, index):
        self.score = score
        self.choice = choice
        self.index = index

    # Method to change score
    def score_method(self, game_outcome):
        if self == winner:
            score += 1

    # Method for choice
    def make_choice(self):
        self.choice = input('rock, paper scissors! Make your choice... ')
        return self.choice
    
    # Method for indexing
    def choice_index(self, choice):
        self.index = RPS.index(self.choice)
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
    player.choice_index(player.choice)
    computer.choice = random.choice(RPS)
    computer.choice_index(computer.choice)
    
    print(computer.choice)
    winner = game_logic(player.index, computer.index)

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
        game_count += 1

print('I won {} games and you won {}'.format(computer.score, player.score))

if computer.score > player.score:
    print('I beat you peasant, worship my awesomeness')
else:
    print('You beat me but you still suck at life and cant code for shit...')

#im less a wizard and more of a hack
