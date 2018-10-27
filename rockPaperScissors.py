#! python3
#rock paper scissors

# MJG: Nice job.  A few things to consider.
#
# Spacing.  See https://www.python.org/dev/peps/pep-0008/ - this provides Python's preferred
# formatting rules.  I follow them... generally.  But there are some good ones like spacing
# around operators.  I changed it according.  Also, you should not name variables with the upper
# case letter 'I' - that's funny because the Python folks specifically call this out. :-)
# 

import random

MAX_GAMES = 3

# list of choices
RPS = ['rock','paper','scissors']


def game_logic_1(player1_choice, player2_choice, player1_score, player2_score):
    """Runs the game logic of rock-paper-scissers.
    `player1_choice` - choice of player 1
    `player2_choice` - choice of player 2
    `player1_score` - current score of player 1
    `player2_score` - current score of player 2

    Returns a tuple of the following info:
    `game_increment` - use this to increment your current running game counter.  In a tie this
    will be 0, otherwise it will be 1.
    `player1_score` - updated score of player 1
    `player2_score` - updated score of player 2
    """

    # Setup a variable to tell the caller how to increment the game_count.  In a tie, this will
    # be zero, otherwise it will be 1.
    game_increment = 0

    if player2_choice == player1_choice:
        print('its a tie!')
        game_increment = 0   # makes sure there can be no tie at the end
    else:
        game_increment = 1

        # sets the rules of rock paper scissors and tracks wins
        #
        # MJG: What about refactoring this into a function that puts the game logic elsewhere?  I'll
        # provide an example below.
        #
        if player2_choice == 'rock':
            if player1_choice == 'paper':
                print('I win!')
                player1_score += 1
            elif player1_choice == 'scissors':
                print('You win')
                player2_score += 1
        elif player2_choice == 'paper':
            if player1_choice == 'rock':
                print('you win')
                player2_score += 1
            elif player1_choice == 'scissors':
                print('I win!')
                conputer_score += 1
        elif player2_choice == 'scissors':
            if player1_choice == 'rock':
                print('I win!')
                player1_score += 1
            elif player1_choice == 'paper':
                print('you win')
                coputer_score += 1

    return game_increment, player1_score, player2_score


def game_logic_2(player1_choice, player2_choice, player1_score, player2_score):
    """Runs the game logic of rock-paper-scissers.  Same as game_logic_1 except it uses
    modulus-indexes to see who's "bigger" than the other.

    `player1_choice` - choice of player 1
    `player2_choice` - choice of player 2
    `player1_score` - current score of player 1
    `player2_score` - current score of player 2

    Returns a tuple of the following info:
    `game_increment` - use this to increment your current running game counter.  In a tie this
    will be 0, otherwise it will be 1.
    `player1_score` - updated score of player 1
    `player2_score` - updated score of player 2
    """

    player1_index = RPS.index(player1_choice);
    player2_index = RPS.index(player2_choice);

    #print("player1_index = {}, player2_index = {}, RPS length = {}".format(player1_index, player2_index, len(RPS)));

    game_increment = 0
    if (player1_index != player2_index):
        game_increment = 1
        # Game on.  Compute the "next" index for player1's choice.  rock -> paper, paper ->
        # scissors, scissors -> rock.
        #
        # MJG: Use the modulus operator (%) to wrap around.  See https://stackoverflow.com/questions/4432208/how-does-work-in-python
        player1_next_index = (player1_index + 1) % len(RPS);

        if (player1_next_index == player2_index):
            player2_score += 1;
        else:
            player1_score += 1;

    return game_increment, player1_score, player2_score





# MJG: Name the variables more clearly and a comment isn't needed.  I renamed to illustrate the
# point.  Also, Python discourages "inline comments" at the end of lines, but sometimes they are
# appropriate, like that one below where you subtract one from the game_count to keep going in
# case of ties.  I thought that was a bug, but then your comment explained it for me.
computer_score = 0
player_score = 0
game_count = 0

print('I challenge you to rock paper scissors, best 2 out of 3!')


# MJG: Usually we define the loop count with a constant, like MAX_GAMES.  Also, generally use
# less-than operator when comparing to the max-loop, rather than less-than-or-equal comparing to
# max-loop minus 1.
#
# MJG: Why bother playing that third game if one person won?  Consider breaking the loop if
# either player's score is greater than MAX_GAMES / 2.

# old: while game_count <= 2:    # loops for 3 rounds
# new:
while game_count < MAX_GAMES:
    print('rock paper scissors!')
    player_choice = raw_input()

    # MJG: Adding a check to make sure you pick a valid value
    if (not player_choice in RPS):
        print("Dude, {} is not a good value.  Don't you know how to play rock paper scissors?  How hard it can be be?  Enter rock, paper, or scissors... DUMB ASS!".format(player_choice))
        continue

    computer_choice = random.choice(RPS)
    print(computer_choice)


    # MJG: Modified to put the game logic into a separate function.  Made it so the old code is
    # still here, but disabled.
    #game_increment, computer_score, player_score = game_logic_1(computer_choice, player_choice, computer_score, player_score)
    game_increment, new_computer_score, new_player_score = game_logic_2(computer_choice, player_choice, computer_score, player_score)

    # MJG: Leave the print-out stuff out of the game logic, do that out here:
    if (game_increment == 0):
        print('its a tie!')
    else:
        if (new_computer_score > computer_score):
            print("I won!  {0} beats {1}... MUTHA FUCKA!!!".format(computer_choice, player_choice))
        else:
            # Must be that player won because the game_increment is non-zero and we know the
            # computer did not win
            print("Screw you!  {0} is truly better than {1}.  This game sucks.".format(computer_choice, player_choice))

    # Save the new scores
    computer_score = new_computer_score
    player_score = new_player_score

    game_count += game_increment


# MJG: Use more sophisticated string formatting rather than '+' to concatenate strings.  All the
# cool kids do it this way.  There are other, better performance mechanisms using 'join', but
# this sort of thing can usually best be done with 'format'.
print('I won {} games, and you won {} games'.format(computer_score, player_score))
if computer_score > player_score:
    print("I beat you!  I'm better.  You're ugly.  Your kids are ugly.  You're the wrong religion")
else:
    print("You are clearly very good at this game.  But you're still a loser in my book")

#im basically a wizard

# MJG: Indeed!
