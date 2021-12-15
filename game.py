global turn
global playing
global board
global winner

turn = "X"
playing = True
board = [
    "#", "#", "#",
    "#", "#", "#",
    "#", "#", "#"
]
winner = "na"

def changeTurn():
    global turn
    if turn == "X":
        changeTurnO()
    elif turn == "O":
        changeTurnX()

def changeTurnO():
    global turn
    turn = "O"

def changeTurnX():
    global turn
    turn = "X"

def checkScore():
    global board
    global playing
    global winner
    
    b1 = board[0]
    b2 = board[1]
    b3 = board[2]
    b4 = board[3]
    b5 = board[4]
    b6 = board[5]
    b7 = board[6]
    b8 = board[7]
    b9 = board[8]
    
    # Left-to-right scores:
    if b1 == "X" and b2 == "X" and b3 == "X":
        playing = False
        winner = "X"
    elif b1 == "O" and b2 == "O" and b3 == "O":
        playing = False
        winner = "O"
    elif b4 == "X" and b5 == "X" and b6 == "X":
        playing = False
        winner = "X"
    elif b4 == "O" and b5 == "O" and b6 == "O":
        playing = False
        winner = "O"
    elif b7 == "X" and b8 == "X" and b9 == "X":
        playing = False
        winner = "X"
    elif b7 == "O" and b8 == "O" and b9 == "O":
        playing = False
        winner = "O"
    #Top-to-bottom scores:
    elif b1 == "X" and b4 == "X" and b7 == "X":
        playing = False
        winner = "X"
    elif b1 == "O" and b4 == "O" and b7 == "O":
        playing = False
        winner = "O"
    elif b2 == "X" and b5 == "X" and b8 == "X":
        playing = False
        winner = "X"
    elif b2 == "O" and b5 == "O" and b8 == "O":
        playing = False
        winner = "O"
    elif b3 == "X" and b6 == "X" and b8 == "X":
        playing = False
        winner = "X"
    elif b3 == "O" and b6 == "O" and b8 == "O":
        playing = False
        winner = "O"
    #Diagonal scores:
    elif b1 == "X" and b5 == "X" and b9 == "X":
        playing = False
        winner = "X"
    elif b1 == "O" and b5 == "O" and b9 == "O":
        playing = False
        winner = "O"
    elif b3 == "X" and b5 == "X" and b7 == "X":
        playing = False
        winner = "X"
    elif b3 == "O" and b5 == "O" and b7 == "O":
        playing = False
        winner = "O"
        

def setBoard(slot):
    global board
    board[slot] = turn

def clearBoard():
    x = 0
    while x < 75:
        print("\n")
        x = x + 1

def drawBoard():
    clearBoard()
    print("Current Player: " + turn)
    print("-------------")
    print("    " + board[0] + " " + board[1] + " " + board[2])
    print("    " + board[3] + " " + board[4] + " " + board[5])
    print("    " + board[6] + " " + board[7] + " " + board[8])
    print("-------------")

def main():
    global board
    global turn
    
    if playing:   
        drawBoard()
        
        slot = int(input("Which slot would you like to choose? (1-9)"))
        slot = slot - 1
        
        if board[slot] == "#":
            setBoard(slot)
        else:
            print("Slot Taken")
            main()
        
        
        checkScore()
        changeTurn()
        main()
    else:
        drawBoard()
        print(winner + " won!")
        quit()

if __name__ == "__main__":
    main()
