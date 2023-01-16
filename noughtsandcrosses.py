# Zaid Darsot
# 2241296
import random
import json
import os.path

# This function draws the board


def draw_board(board):
    for row in board:
        print(' -----------')
        for col in row:
            print('|', col, end=' ')
        print('|')
    print(' -----------')
    return board

# This function displays the welcome message


def welcome(board):
    print("Welcome to the unbeatable Noughts and Crosses game.")
    print("The board layout is shown below: ")
    print(" -----------")
    print("| 1 | 2 | 3 |")
    print(" -----------")
    print("| 4 | 5 | 6 |")
    print(" -----------")
    print("| 7 | 8 | 9 |")
    print(" -----------")
    print("When prompted, enter the number corresponding to the square you want.")
    return (board)

# This Function initialises the board


def initialise_board(board):
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board

# This Function gets move from the player


def get_player_move(board):

    while True:
        num = input("Choose Your Square from 1-9: ")
        if num.isdigit:
            num = int(num)
            if num >= 1 and num <= 9:
                row = (num-1)//3
                col = (num-1) % 3
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    break

        print("Invalid Cell")

    return board

# This Function makes the computer choose a move


def choose_computer_move(board):
    try:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == ' ':
            board[row][col] = 'O'
        else:
            choose_computer_move(board)
        return row, col
    except RecursionError:
        pass

# This function checks for win


def check_for_win(board, mark):
    if board[0][0] == mark and board[0][1] == mark and board[0][2] == mark:
        return True
    elif board[1][0] == mark and board[1][1] == mark and board[1][2] == mark:
        return True
    elif board[2][0] == mark and board[2][1] == mark and board[2][2] == mark:
        return True
    elif board[0][0] == mark and board[1][1] == mark and board[2][2] == mark:
        return True
    elif board[0][2] == mark and board[1][1] == mark and board[2][0] == mark:
        return True
    elif board[0][0] == mark and board[1][0] == mark and board[2][0] == mark:
        return True
    elif board[0][1] == mark and board[1][1] == mark and board[2][1] == mark:
        return True
    elif board[0][2] == mark and board[1][2] == mark and board[2][2] == mark:
        return True
    else:
        return False

# This Function checks for draw


def check_for_draw(board):
    for row in range(0, 3):
        for col in range(0, 3):
            if board[row][col] == ' ':
                return False
    return True

# This function is for playing the game


def play_game(board):
    board = initialise_board(board)
    draw_board(board)
    mark = 'X'
    while check_for_win(board, mark) == False and check_for_draw(board) == False:
        get_player_move(board)
        mark = 'X'
        check_for_win(board, mark)
        if check_for_win(board, mark) == True:
            draw_board(board)
            print("Player Wins")
            print("Game over")
            return 1

        elif check_for_win(board, mark) == False:
            check_for_draw(board)
            if check_for_draw(board) == True:
                draw_board(board)
                print("Tie")
                print("Game over")
                return 0

        choose_computer_move(board)
        draw_board(board)
        mark = "O"
        check_for_win(board, mark)
        if check_for_win(board, mark) == True:
            draw_board(board)
            print("Computer wins")
            print("Game over")
            return -1
        elif check_for_win(board, mark) == False:
            check_for_draw(board)
            if check_for_draw(board) == True:
                draw_board(board)
                print("Tie")
                print("Game over")
                return 0

# This Function prints menu


def menu():

    print("-----Menu-----")
    print("Choose one of the following options: ")
    print("1-Play the game")
    print("2-Save your score in the leaderboard")
    print("3-Load and Display the leaderboard")
    print("q-End the Process")
    choice = (input("1,2,3 or q ? - "))
    if choice in ['1', '2', '3', 'q']:
        return choice
    else:
        print("Invalid choice. Please enter 1, 2, 3 or q.")
    return choice

# This Function loads the scores


def load_scores():
    if os.path.isfile('leaderboard.txt'):
        with open('leaderboard.txt', 'r') as f:
            leaders = json.load(f)
    else:
        leaders = {}
    return leaders

# This Function saves your scores


def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    if name in leaders:
        leaders[name] += score
    else:
        leaders[name] = score
    with open('leaderboard.txt', 'w') as f:
        json.dump(leaders, f)
    return

# This function displays the leaderboard


def display_leaderboard(leaders):
    leaders_list = [(k, v) for k, v in leaders.items()]
    leaders_list.sort(key=lambda x: x[1], reverse=True)
    print("Leaderboard:")
    for i, (name, score) in enumerate(leaders_list):
        print(f"{i + 1}. {name}: {score}")
