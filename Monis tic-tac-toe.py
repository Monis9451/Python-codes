import os
import sys
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
player1=input("Enter player1 name: ")
player2=input("Enter player2 name: ")
p1s = "X"
p2s = "O"
currentPlayer=player1
currentSlymbol=p1s
print(f"{player1}'s symbol is {p1s} ")
print(f"{player2}'s symbol is {p2s} ")
def printboard():
    for i in range (3):
        for j in range (3):
            print(board[i][j],end=" ")
            if(j==0 or j==1):
                print(" ","|",end=" ")
        print("\n",end="")
        if(i<2):
            print("---------------")
            
def mark(symbol,row,coulmn):
    board[row][coulmn]=symbol

def Wincheck(player):
    if(board[0][0]==board[0][1]==board[0][2]==player or
       board[1][0]==board[1][1]==board[1][2]==player or
       board[2][0]==board[2][1]==board[2][2]==player or
       board[0][0]==board[1][0]==board[2][0]==player or
       board[0][1]==board[1][1]==board[2][1]==player or
       board[0][2]==board[1][2]==board[2][2]==player or
       board[0][0]==board[1][1]==board[2][2]==player or
       board[0][2]==board[1][1]==board[2][0]==player):
        
        if(player==p1s):
            os.system("cls")
            print(f"{player1} WINS and {player2} LOSES")
            return False
        else:
            os.system("cls")
            print(f"{player2} WINS and {player1} LOSES")
            return False
    else:
        return True    

def TakeInput(player):
    while True:
        try:
            R = int(input(f"{player} enter the row of matrix (1-3): ")) - 1
            C = int(input(f"{player} enter the column of matrix (1-3): ")) - 1
            index=[R,C]
            if R not in range(3) or C not in range(3):
                print("Invalid inputs! Please enter row and column between 1 and 3.")
                continue
            if board[R][C] != " ":
                print("This index is already taken! Try again.")
                continue
            return index
        except ValueError:
            print("Invalid input! Please enter numbers(1-3) only.")
       
def Checkdraw():
    draw=0     
    for i in range (3):
        for j in range (3):
            if(board[i][j]==" "):
                draw += 1
    if (draw<1):
           print("The game is draw!")
           sys.exit()
        
while(True):
    os.system("cls")
    printboard()
    index=TakeInput(currentPlayer)
    mark(currentSlymbol,index[0],index[1])
    winCheck=Wincheck(currentSlymbol)
    Checkdraw()
    if(winCheck):
        if(currentPlayer==player1 and currentSlymbol==p1s):
            currentPlayer=player2
            currentSlymbol=p2s
        elif(currentPlayer==player2 and currentSlymbol==p2s):
            currentPlayer=player1
            currentSlymbol=p1s
    else:
        break
printboard()

import os
import sys
board=[[" "," "," "],[" "," "," "],[" "," "," "]]
player1=input("Enter player1 name: ")
player2=input("Enter player2 name: ")
p1s = "X"
p2s = "O"
currentPlayer=player1
currentSlymbol=p1s
print(f"{player1}'s symbol is {p1s} ")
print(f"{player2}'s symbol is {p2s} ")
def printboard():
    for i in range (3):
        for j in range (3):
            print(board[i][j],end=" ")
            if(j==0 or j==1):
                print(" ","|",end=" ")
        print("\n",end="")
        if(i<2):
            print("---------------")
            
def mark(symbol,row,coulmn):
    board[row][coulmn]=symbol

def Wincheck(player):
    if(board[0][0]==board[0][1]==board[0][2]==player or
       board[1][0]==board[1][1]==board[1][2]==player or
       board[2][0]==board[2][1]==board[2][2]==player or
       board[0][0]==board[1][0]==board[2][0]==player or
       board[0][1]==board[1][1]==board[2][1]==player or
       board[0][2]==board[1][2]==board[2][2]==player or
       board[0][0]==board[1][1]==board[2][2]==player or
       board[0][2]==board[1][1]==board[2][0]==player):
        
        if(player==p1s):
            os.system("cls")
            print(f"{player1} WINS and {player2} LOSES")
            return False
        else:
            os.system("cls")
            print(f"{player2} WINS and {player1} LOSES")
            return False
    else:
        return True    

def TakeInput(player):
    while True:
        try:
            R = int(input(f"{player} enter the row of matrix (1-3): ")) - 1
            C = int(input(f"{player} enter the column of matrix (1-3): ")) - 1
            index=[R,C]
            if R not in range(3) or C not in range(3):
                print("Invalid inputs! Please enter row and column between 1 and 3.")
                continue
            if board[R][C] != " ":
                print("This index is already taken! Try again.")
                continue
            return index
        except ValueError:
            print("Invalid input! Please enter numbers(1-3) only.")
       
def Checkdraw():
    draw=0     
    for i in range (3):
        for j in range (3):
            if(board[i][j]==" "):
                draw += 1
    if (draw<1):
           print("The game is draw!")
           sys.exit()
        
while(True):
    os.system("cls")
    printboard()
    index=TakeInput(currentPlayer)
    mark(currentSlymbol,index[0],index[1])
    winCheck=Wincheck(currentSlymbol)
    Checkdraw()
    if(winCheck):
        if(currentPlayer==player1 and currentSlymbol==p1s):
            currentPlayer=player2
            currentSlymbol=p2s
        elif(currentPlayer==player2 and currentSlymbol==p2s):
            currentPlayer=player1
            currentSlymbol=p1s
    else:
        break
printboard()