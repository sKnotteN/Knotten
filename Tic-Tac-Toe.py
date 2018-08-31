"""
Author: Kristian Saure Knotten
Student ID: 8284
E-mail: ksknotten@outlook.com
"""

# Import libs
from random import randint
from time import sleep

# Set variables
board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']
done = False
taken = set()


# Check if the chosen value is already taken or if its over 9 or under 1.
def setX(num, player):
    global taken
    global board
    if num not in taken:
        if 0 <= num <= 8:
            checkplayer(num, player)
            return True
        else:
            print('number to high or low')
            return False
    else:
        print('number %s is taken\n' % str(num + 1))


# check which player it is and add the right mark to the board
def checkplayer(num, player):
    global board
    if player == 1:
        board[num] = 'X'
        taken.add(num)
    elif player == 2:
        board[num] = 'O'
        taken.add(num)
    else:
        print('Something went wrong with the player number')


# Go threw and check if the board has a winner
def checkwin(mark, player):
    global done
    if board[0] == mark and board[1] == mark and board[2] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(0, 1, 2, mark)
        done = True
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(3, 4, 5, mark)
        done = True
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(6, 7, 8, mark)
        done = True
        return True
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(0, 3, 6, mark)
        done = True
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(1, 4, 7, mark)
        done = True
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(2, 5, 8, mark)
        done = True
        return True
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(0, 4, 8, mark)
        done = True
        return True
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        print('\nPlayer %s is the winner!' % player)
        winprint(2, 4, 6, mark)
        done = True
        return True
    elif ' ' not in board:
        print("\nIt's a draw!")
        printboard()
        done = True
        return True
    else:
        pass
    printboard()


# Print out the current board
def printboard():
    print('\t', board[0], '|', board[1], '|', board[2],
          '\n\t --|---|--\n',
          '\t', board[3], '|', board[4], '|', board[5],
          '\n\t --|---|--\n',
          '\t', board[6], '|', board[7], '|', board[8], '\n')


# Print out the winning row
def winprint(num1, num2, num3, player):
    winningboard = [' ', ' ', ' ',
                    ' ', ' ', ' ',
                    ' ', ' ', ' ']
    winningboard[num1] = player
    winningboard[num2] = player
    winningboard[num3] = player
    print('The winning row:\n')
    print('\t', winningboard[0], '|', winningboard[1], '|', winningboard[2],
          '\n\t --|---|--\n',
          '\t', winningboard[3], '|', winningboard[4], '|', winningboard[5],
          '\n\t --|---|--\n',
          '\t', winningboard[6], '|', winningboard[7], '|', winningboard[8])


# Comp picks a random number. If the number is already taken he tries a one.
def compPick():
    while True:
        choice = randint(0, 8)
        if choice not in taken:
            setX(choice, 2)
            checkwin('O', 2)
            break
        else:
            pass


# Player 2 picks a number. If the number is already taken then try again
def player2Pick():
    while True:
        choice = int(input('Playere 2 pick a number: '))
        valid = setX(choice - 1, 2)
        # If the number choice is valid, check if the player won; if not the computer takes a turn
        if valid:
            checkwin('O', 2)
            break
        else:
            pass


# Start up singleplayer and ask the user to pick a number between 1 and 9
def multiplayer():
    while not done:
        try:
            choice = int(input('Player 1 pick a number: '))
            valid = setX(choice - 1, 1)
            # If the number choice is valid, check if the player won; if not the computer takes a turn
            if valid:
                won = checkwin('X', 1)
                if not won:
                    player2Pick()
            else:
                pass

        except ValueError:
            print('Please type in a number')


# Start up multiplayer and player one picks the first number
def singleplayer():
    while not done:
        try:
            choice = int(input('Pick a number: '))
            valid = setX(choice - 1, 1)
            # If the number choice is valid, check if the player won; if not the computer takes a turn
            if valid:
                won = checkwin('X', 1)
                if not won:
                    sleep(1)
                    compPick()
            else:
                pass
        except ValueError:
            print('Please type in a number')

# Print out information about what this program does
print('\nThis is a tic tac toe game. To place your mark choose a number between 1 and 9')
print('1 | 2 | 3\n'
      '--|---|--\n'
      '4 | 5 | 6\n'
      '--|---|--\n'
      '7 | 8 | 9\n')
print('You can play against a computer or against another player')


# Ask the user if he wants to player single or multiplayer
while True:
    ask = input('Would you like to play single or multiplayer? Type in single or multi: ')
    if ask.lower() == 'single':
        singleplayer()
        break
    elif ask.lower() == 'multi':
        multiplayer()
        break
    else:
        print('Please choose between "multi" and "single"\n')
