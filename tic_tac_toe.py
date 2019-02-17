def display_board(board):
    matrix = {
        'one': board[1],
        'two': board[2],
        'three' : board[3],
        'four' : board[4],
        'five' : board[5],
        'six' : board[6],
        'seven' : board[7],
        'eight' : board[8],
        'nine' : board[9]
    }


    print("""
              {} | {} | {}
             --- --- ---
              {} | {} | {}
             --- --- ---
              {} | {} | {}

              """.format(matrix['one'],matrix['two'],matrix['three'],matrix['four'],matrix['five'],
                         matrix['six'],matrix['seven'],matrix['eight'],matrix['nine']))

def player_input():
    ready1 = False
    ready2 = False
    while ready1 == False:
        player_select = input("Are you Player one [X] or two [O]? [1,2] ")
        player_nr = int(player_select)
        if player_nr in range(1,3):
            ready1 = True
            if player_nr == 1:
                return "X"
            else:
                return "O"

            ready2 = True

def place_marker(board, marker, position):
    board[int(position)] = marker

def win_check(board, mark):
    winner_list = [board[1:4],board[4:7],board[7:10],board[1:8:3],board[2:10:3],board[3:10:3],board[1:10:4],board[3:8:2]]
    if [mark,mark,mark] in winner_list:
        return True
    else:
        return False

def choose_first():
    import random
    if random.randint(0,10)%2 > 0:
        return int(1)
    else:
        return int(2)

def space_check(board, position):
    #print(board[position])
    return (board[position] != "O" and board[position] != "X")

def full_board_check(board):
    return " " not in board


def player_choice(board):
    my_repeat = True
    while my_repeat:
        what_next = int(input('What is your next move [1-9]? '))
        if what_next not in list(range(1,10)):
            my_repeat = True
            pass
        elif space_check(board,what_next):
                my_repeat = False
                return int(what_next)
        elif full_board_check:
            break
        my_repeat = True


def replay():
    return 'y' == input('You want to go again [y/n]? ')



active_player = choose_first()
marker_player1 = player_input()
if marker_player1 == 'X':
    marker_player2 = 'O'
else:
    marker_player2 = 'X'

while True:

    print('Welcome to Tic Tac Toe! See the empty Board, the world is your Oyster')
    play_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(play_board)

    while not full_board_check(play_board):

        print('Player 1 your turn')
        move1 = player_choice(play_board)
        place_marker(play_board,marker_player1,move1)
        display_board(play_board)
        if win_check(play_board,marker_player1):
            print('You Win Player 1')
            display_board(play_board)
            break

        print('Player 2 your turn')
        move2 = player_choice(play_board)
        place_marker(play_board,marker_player2,move2)
        display_board(play_board)
        if win_check(play_board,marker_player2):
            print('You Win Player 2')
            display_board(play_board)
            break

        if full_board_check(play_board):
            print('Neither of you won - you are either equally smart or dumb')
            break

    if replay() == False:
        print('thank you for playing')
        break
