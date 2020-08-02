game_logic = True
winner = None
curr_player = "X"
board = [["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]]

def compTurn():
    bestScore = -999
    move = None
    for x in range(3):
        for y in range(3):
            if board[x][y] == "-":
                board[x][y] = "O"
                score = minimax(board,0,False)
                board[x][y] = "-"
                if score>bestScore:
                    bestScore=score
                    move = (x,y)
    board[move[0]][move[1]] = "O"
    display_board()

def minimax(board,depth,isMaximizing):
    result = checkWinTest()
    if result != None:
        if result == "X":
            return -10
        elif result == "O":
            return 10
        else:
            return 0
    if(isMaximizing):
        bestScore = -999
        for x in range(3):
            for y in range(3):
                if board[x][y] == "-":
                    board[x][y] = "O"
                    score = minimax(board,depth+1,False)
                    board[x][y] = "-"
                    bestScore=max(score,bestScore)
        return bestScore
    else:
        bestScore = 999
        for x in range(3):
            for y in range(3):
                if board[x][y] ==  "-":
                    board[x][y] = "X"
                    score = minimax(board,depth+1,True)
                    board[x][y] = "-"
                    bestScore = min(score,bestScore)
        return bestScore
    
def display_board():
    print("\n")
    print(board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "     1 | 2 | 3")
    print(board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "     4 | 5 | 6")
    print(board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "     7 | 8 | 9")
    print("\n")

def checkWin():
    global game_logic
    row_1 = board[0][0] == board[0][1] == board[0][2] != "-"
    row_2 = board[1][0] == board[1][1] == board[1][2] != "-"
    row_3 = board[2][0] == board[2][1] == board[2][2] != "-"
    col_1 = board[0][0] == board[1][0] == board[2][0] != "-"
    col_2 = board[0][1] == board[1][1] == board[2][1] != "-"
    col_3 = board[0][2] == board[1][2] == board[2][2] != "-"
    diag_1 = board[0][0] == board[1][1] == board[2][2] != "-"
    diag_2 = board[0][2] == board[1][1] == board[2][0] != "-"
    if row_1 or row_2 or row_3 or col_1 or col_2 or col_3 or diag_1 or diag_2:
        game_logic=False
    if row_1:
        return board[0][0]
    elif row_2:
        return board[1][0]
    elif row_3:
        return board[2][0]
    elif col_1:
        return board[0][0]
    elif col_2:
        return board[0][1]
    elif col_3:
        return board[0][2]
    elif diag_1:
        return board[0][0]
    elif diag_2:
        return board[0][2]
    elif "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
        game_logic = False
        print("Board Full")
        return "Tie"

def checkWinTest():
    row_1 = board[0][0] == board[0][1] == board[0][2] != "-"
    row_2 = board[1][0] == board[1][1] == board[1][2] != "-"
    row_3 = board[2][0] == board[2][1] == board[2][2] != "-"
    col_1 = board[0][0] == board[1][0] == board[2][0] != "-"
    col_2 = board[0][1] == board[1][1] == board[2][1] != "-"
    col_3 = board[0][2] == board[1][2] == board[2][2] != "-"
    diag_1 = board[0][0] == board[1][1] == board[2][2] != "-"
    diag_2 = board[0][2] == board[1][1] == board[2][0] != "-"
    if row_1:
        return board[0][0]
    elif row_2:
        return board[1][0]
    elif row_3:
        return board[2][0]
    elif col_1:
        return board[0][0]
    elif col_2:
        return board[0][1]
    elif col_3:
        return board[0][2]
    elif diag_1:
        return board[0][0]
    elif diag_2:
        return board[0][2]
    elif "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
        return "Tie"

def flip_player():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"

def playerTurn(curr_player):
    print(curr_player+"'s turn.")
    position = input("Choose a position form 1-9: ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position form 1-9: ")

        if position == "1":
            pos1 = 0
            pos2 = 0
        elif position == "2":
            pos1 = 0
            pos2 = 1
        elif position == "3":
            pos1 = 0
            pos2 = 2
        elif position == "4":
            pos1 = 1
            pos2 = 0
        elif position == "5":
            pos1 = 1
            pos2 = 1
        elif position == "6":
            pos1 = 1
            pos2 = 2
        elif position == "7":
            pos1 = 2
            pos2 = 0
        elif position == "8":
            pos1 = 2
            pos2 = 1
        else:
            pos1 = 2
            pos2 = 2

        if board[pos1][pos2] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")
            position = input("Choose a position form 1-9: ")

    board[pos1][pos2] = curr_player

    display_board()

def main():
    

    # ------ Game Here ------
    display_board()

    while game_logic:
        playerTurn(curr_player)
        winner=checkWin()
        if winner == "X" or winner =="O":
            print(winner+" won.")
            break
        elif winner == "Tie":
            print("Tie.")
            break
        compTurn()
        winner=checkWin()
        if winner == "X" or winner =="O":
            print(winner+" won.")
            break
        elif winner == "Tie":
            print("Tie.")
            break



if __name__ == '__main__':
    main()