import time
import os

def clear():
    return os.system('cls')


def print_board():
    for boarder in board:
        print("".join(boarder))
        

def functionallity(number):
    clear = 2
    next_line = 1

    add_row = -2
    add_col = 2
    
    for row in range(len(board)):
        for col in range(len(board)):
            if row + number == 7 + number and col == 7 and row + number < len(board) - 1:
                board[row + number][col] = "*"
            
            if board[add_row][7] == "*":
                if col + clear < len(board) - next_line and next_line < len(board) - 1:
                    if board[next_line][clear] == " ":
                        next_line += 1
                        clear += 1
                        add_row -= 1
                        add_col += 1

                    else:
                        board[next_line][clear] = " "
                        board[add_row][add_col] = "*"
                        clear += 1
                        add_col += 1

    return add_row

board = [
    [" ","-","-","-","-","-","-","-","-","-","-","-","-","-"," "],
    [" ","\\","*","*","*","*","*","*","*","*","*","*","*","/"," "],
    [" "," ","\\","*","*","*","*","*","*","*","*","*","/"," "," "],
    [" "," "," ","\\","*","*","*","*","*","*","*","/"," "," "," "],
    [" "," "," "," ","\\","*","*","*","*","*","/"," "," "," "," "],
    [" "," "," "," "," ","\\","*","*","*","/",""," "," "," "," "],
    [" "," "," "," "," "," ","\\","*","/",""," "," "," "," "," "],
    [" "," "," "," "," "," ","/"," ","\\"," "," "," "," "," "," "],
    [" "," "," "," "," ","/"," "," "," ","\\"," "," "," "," "," "],
    [" "," "," "," ","/"," "," "," "," "," ","\\"," "," "," "," "],
    [" "," "," ","/"," "," "," "," "," "," "," ","\\"," "," "," "],
    [" "," ","/"," "," "," "," "," "," "," "," "," ","\\"," "," "],
    [" ","/"," "," "," "," "," "," "," "," "," "," "," ","\\"," "],
    [" ","-","-","-","-","-","-","-","-","-","-","-","-","-"," "]


]


number = 0

while True:

    time.sleep(0.20)
    clear()

    print_board()
    test = functionallity(number)
    
    if test == -8:
        # TODO : Create functionallity for rotete the clock
        
        pass
        

    number += 1
