# print the board
def print_board(board):
    for row in reversed(board):
        for col in row:
            print(col, end=' ')
        print()


# initialize the board
def initialize_board(num_rows, num_cols):
    board = [["-" for i in range(0, num_rows)] for j in range(0, num_cols)]

    return board


# enter chip in column
def insert_chip(board, col, chip_type):
    row = ""
    for i in range(0, len(board)):
        if board[i][col] == '-':
            board[i][col] = chip_type
            row = i
            break
    return row


# check for 4 consecutive 'x' or 'o'
def check_if_winner(board, col, row, chip_type):
    # check horizontally
    consecutive = 0
    for i in range(0, len(board[row])):
        if board[row][i] == chip_type:
            consecutive += 1
            if consecutive == 4:
                return True
        else:
            consecutive = 0

    # check vertically
    consecutive = 0
    for i in range(0, len(board)):
        if board[i][col] == chip_type:
            consecutive += 1
            if consecutive == 4:
                return True
        else:
            consecutive = 0


# main function for all the user input
def main():
    height = int(input("What would you like the height of the board to be? "))
    width = int(input("What would you like the length of the board to be? "))
    board = initialize_board(width, height)
    print_board(board)
    print("Player 1: x")
    print("Player 2: o")

    continue_game = True
    current_player = 'player_1'
    while continue_game:
        if current_player == 'player_1':
            player1_col = int(input("Player 1: Which column would you like to choose? "))
            row = insert_chip(board, player1_col, 'x')
            # check for 4 consecutive 'x'
            if check_if_winner(board, player1_col, row, 'x'):
                print_board(board)
                print("Player 1 won the game!")
                continue_game = False
            # check if there is no more '-'
            else:
                game_draw = 'yes'
                for row in range(0, len(board)):
                    for col in range(0, len(board[row])):
                        if board[row][col] == '-':
                            game_draw = 'no'
                            break
                        else:
                            continue
                if game_draw == 'yes':
                    print_board(board)
                    print("Draw. Nobody wins.")
                    continue_game = False

            current_player = 'player_2'
        else:
            player2_col = int(input("Player 2: Which column would you like to choose? "))
            row = insert_chip(board, player2_col, 'o')
            # check for 4 consecutive 'o'
            if check_if_winner(board, player2_col, row, 'o'):
                print_board(board)
                print("Player 2 won the game!")
                continue_game = False
            # check if there is no more '-'
            else:
                game_draw = 'yes'
                for row in range(0, len(board)):
                    for col in range(0, len(board[row])):
                        if board[row][col] == '-':
                            game_draw = 'no'
                            break
                        else:
                            continue
                if game_draw == 'yes':
                    print_board(board)
                    print("Draw. Nobody wins.")
                    continue_game = False
            current_player = 'player_1'

        if continue_game:
            print_board(board)

if __name__ == "__main__":
    main()
