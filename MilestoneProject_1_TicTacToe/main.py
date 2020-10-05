import random
from os import system


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    while True:
        xo = input('\nPlayer 1 -> Choose "X" or "O" : ').upper()
        if xo == 'X':
            return 'X', 'O'
        elif xo == 'O':
            return 'O', 'X'
        else:
            print('Enter Valid Input')
            pass


def place_marker(board, marker, pos):
    board[pos] = marker


def win_check(board, mark):
    # Cross the Top, Middle and Bottom
    # Down the Left, Middle and Right
    # Diagonal
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[8] == board[5] == board[2] == mark) or
            (board[9] == board[6] == board[3] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[9] == board[5] == board[1] == mark))


def choose_first():
    rand = random.randrange(1, 3)
    if rand == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, pos):
    return board[pos] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, pos):
        pos = int(input('Choose a position: (1-9) '))
    return pos


def replay():
    choice = input('Play Again? (Y/N) : ').upper()
    return choice == 'Y'


def game_manager():
    system('cls')
    print('\t\t\t\t\t\t\tWelcome to TicTacToe')
    while True:
        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()
        print(f'\nPlayer 1 -> {player1_marker}')
        print(f'Player 2 -> {player2_marker}')

        turn = choose_first()
        print(f'\n{turn}, will go first')

        play_game = input('Ready? (Y/N) : ').upper()
        if play_game == 'Y':
            game_on = True
        else:
            game_on = False

        while game_on:
            system('cls')
            if turn == 'Player 1':
                # Show Board
                display_board(the_board)
                # Choose Position
                pos = player_choice(the_board)
                # Place the marker on the position
                place_marker(the_board, player1_marker, pos)
                # Check if they won
                if win_check(the_board, player1_marker):
                    system('cls')
                    display_board(the_board)
                    print('PLAYER 1 HAS WON!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        system('cls')
                        display_board(the_board)
                        print('TIE!!')
                        game_on = False
                    else:
                        turn = 'Player 2'
            else:
                # Show Board
                display_board(the_board)
                # Choose Position
                pos = player_choice(the_board)
                # Place the marker on the position
                place_marker(the_board, player2_marker, pos)
                # Check if they won
                if win_check(the_board, player2_marker):
                    system('cls')
                    display_board(the_board)
                    print('PLAYER 2 HAS WON!!')
                    game_on = False
                else:
                    if full_board_check(the_board):
                        system('cls')
                        display_board(the_board)
                        print('TIE!!')
                        game_on = False
                    else:
                        turn = 'Player 1'
        if not replay():
            break


game_manager()
