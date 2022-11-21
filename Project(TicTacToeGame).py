import random


def display_board(board):
    positionIndex = 1
    # Printing each sign in the list abased on the position index
    for i in board:
        # Signs at these position indexs print extra line
        if positionIndex not in [3, 6, 9]:
            print(i, "| ", end="")
        else:
            print(i, "\n", end="")
            print("----------")
        positionIndex += 1
    return


def player_input():
    # Asking the player input for the first player's mark choice
    while True:
        player1Mark = input("Player 1: Do you want to be X or O?\n")
        if player1Mark not in ["X", "O"]:
            print("Please select X or O")
        else:
            if player1Mark == 'X':
                player2Mark = 'O'
            else:
                player2Mark = 'X'
            return (player1Mark, player2Mark)


def place_marker(board, marker, position):
    # Placing marker at the position index of the board
    board[position-1] = marker
    return


def win_check(board, mark):
    # checks to see if that mark has won
    if board[0:3] == [mark, mark, mark] or board[3:6] == [mark, mark, mark] or board[6:9] == [mark, mark, mark] or board[0:7:3] == [mark, mark, mark] or board[1:8:3] == [mark, mark, mark] or board[2:9:3] == [mark, mark, mark] or board[0:9:4] == [mark, mark, mark] or board[2:7:2] == [mark, mark, mark]:
        win = True
    else:
        win = False
    return win


def choose_first():
    # Randomly decide which player goes first
    whichPlayer = random.randint(1, 2)
    if whichPlayer == 1:
        print("Player 1 will go first.")
    else:
        print("Player 2 will go first.")
    return whichPlayer


def space_check(board, position):
    # Whether a space on the board is freely available
    if board[position-1] != ' ':
        return False
    else:
        return True


def full_board_check(board):
    # Checks if the board is full. True if full, False otherwise.
    fullCheck = 0
    for i in board:
        if i == ' ':
            fullCheck += 1
    if fullCheck == 0:
        return True
    else:
        return False


def player_choice(board):
    # Asks for a player's next position and then uses the space_check function to check if it's a free position. If it is, then return the position for later use.
    while True:
        try:
            position = int(input("Choose your next position: (1-9):\n"))
            if 0 < position < 10:
                if space_check(board, position):
                    return position
                else:
                    print('\n'*100)
                    print(
                        "The position you selected is not free, please select another position.")
                    display_board(board)
            else:
                raise ValueError
        except ValueError:
            print("Please select position between 1-9")


def replay():
    # Asks the player if they want to play again and returns a boolean True if they do want to play again
    while True:
        playAgain = input("Do you want to play again? Enter Yes or No:\n")
        if playAgain == "Yes":
            return True
        elif playAgain == "No":
            print("Thank you for playing, see you!")
            return False
        else:
            print("Please enter Yes or No")


gameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
print('Welcome to Tic Tac Toe!')
while True:
    # Set the game up here
    player1, player2 = player_input()
    whoseTurn = choose_first()
    ready = False
    while ready == False:
        readyPlayer = input("Are you ready to play? Enter Yes or No.\n")
        if readyPlayer == "Yes":
            game_on = True
            ready = True
        elif readyPlayer == "No":
            print("OK, see you!")
            break
        else:
            print("Please enter Yes or No")
    # Game starts here
    while game_on:
        if whoseTurn == 1:
            # Player 1 Turn
            display_board(gameBoard)
            if full_board_check(gameBoard):
                print("Sorry, the game board is full. The game ended and nobody won.")
                break
            position = player_choice(gameBoard)
            place_marker(gameBoard, player1, position)
            print('\n'*100)
            if win_check(gameBoard, player1):
                display_board(gameBoard)
                print("Congratulations! You have won the game!")
                break
            display_board(gameBoard)
            if full_board_check(gameBoard):
                print("Sorry, the game board is full. The game ended and nobody won.")
                break
            position = player_choice(gameBoard)
            place_marker(gameBoard, player2, position)
            print('\n'*100)
            if win_check(gameBoard, player2):
                display_board(gameBoard)
                print("Congratulations! You have won the game!")
                break
        else:
            # Player2's turn.
            display_board(gameBoard)
            if full_board_check(gameBoard):
                print("Sorry, the game board is full. The game ended and nobody won.")
                break
            position = player_choice(gameBoard)
            place_marker(gameBoard, player2, position)
            print('\n'*100)
            if win_check(gameBoard, player2):
                display_board(gameBoard)
                print("Congratulations! You have won the game!")
                break
            display_board(gameBoard)
            if full_board_check(gameBoard):
                print("Sorry, the game board is full. The game ended and nobody won.")
                break
            position = player_choice(gameBoard)
            place_marker(gameBoard, player1, position)
            print('\n'*100)
            if win_check(gameBoard, player1):
                display_board(gameBoard)
                print("Congratulations! You have won the game!")
                break
    if not replay():
        break
    else:
        gameBoard = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
