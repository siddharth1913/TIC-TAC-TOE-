import random
print("\nWelcome to Tic Tac Toe\n")

possibleNum = [1,2,3,4,5,6,7,8,9]
gameBoard = [[" "," "," "],[" "," "," "],[" "," "," "]]
row = 3
col = 3

def printgameBoard():
    for i in range(row):
        print("\n-------------")
        print("|",end="")
        for j in range(col):
            print("",gameBoard[i][j], end=" |")
    print("\n-------------\n")

def modifyarray(num,turn):
    num-=1
    if(num == 0):
        gameBoard[0][0] = turn
    elif(num == 1):
        gameBoard[0][1] = turn
    elif(num == 2):
        gameBoard[0][2] = turn
    elif(num == 3):
        gameBoard[1][0] = turn
    elif(num == 4):
        gameBoard[1][1] = turn
    elif(num == 5):
        gameBoard[1][2] = turn
    elif(num == 6):
        gameBoard[2][0] = turn
    elif(num == 7):
        gameBoard[2][1] = turn
    elif(num == 8):
        gameBoard[2][2] = turn
    
def Winner(gameBoard):
    if(gameBoard[0][0]=='X' and gameBoard[0][1]=='X' and gameBoard[0][2]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[0][1]=='O' and gameBoard[0][2]=='O'):
        print("CPU won the game\n")
        return 'O'
    elif(gameBoard[1][0]=='X' and gameBoard[1][1]=='X' and gameBoard[1][2]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[1][0]=='O' and gameBoard[1][1]=='O' and gameBoard[1][2]=='O'):
        print("CPU won the game\n")
        return 'O'
    elif(gameBoard[2][0]=='X' and gameBoard[2][1]=='X' and gameBoard[2][2]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[2][0]=='O' and gameBoard[2][1]=='O' and gameBoard[2][2]=='O'):
        print("CPU won the game\n")
        return 'O'
    

    if(gameBoard[0][0]=='X' and gameBoard[1][0]=='X' and gameBoard[2][0]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[1][0]=='O' and gameBoard[2][0]=='O'):
        print("CPU won the game\n")
        return 'O'
    elif(gameBoard[0][1]=='X' and gameBoard[1][1]=='X' and gameBoard[2][1]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[0][1]=='O' and gameBoard[1][1]=='O' and gameBoard[2][1]=='O'):
        print("CPU won the game\n")
        return 'O'
    elif(gameBoard[0][2]=='X' and gameBoard[1][2]=='X' and gameBoard[2][2]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[0][2]=='O' and gameBoard[1][2]=='O' and gameBoard[2][2]=='O'):
        print("CPU won the game\n")
        return 'O'
    

    if(gameBoard[0][0]=='X' and gameBoard[1][1]=='X' and gameBoard[2][2]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[0][0]=='O' and gameBoard[1][1]=='O' and gameBoard[2][2]=='O'):
        print("CPU won the game\n")
        return 'O'
    elif(gameBoard[0][2]=='X' and gameBoard[1][1]=='X' and gameBoard[2][0]=='X'):
        print("You won the game\n")
        return 'X'
    elif(gameBoard[0][2]=='O' and gameBoard[1][1]=='O' and gameBoard[2][0]=='O'):
        print("CPU won the game\n")
        return 'O'
    else:
        return 'N'
    


leaveloop = False
whosturn = 0

while(leaveloop == False):
    if(whosturn % 2 == 1):
        printgameBoard()
        numpick = int(input("PLAYER 2 : Choose the number between [1-9] : "))
        if(numpick >= 1 and numpick <= 9):
            modifyarray(numpick,'X')
            possibleNum.remove(numpick)
        else:
            print("Enter the Valid positions\n")
        whosturn += 1 
    else:
        while (True):

            # This logic is for one player game  

            cpuChoice = random.choice(possibleNum)
            print("\ncpuchoose the number : ",cpuChoice)

            if(cpuChoice in possibleNum):
                modifyarray(cpuChoice,'O')
                possibleNum.remove(cpuChoice)
                whosturn += 1
                break
            
            # printgameBoard()
            # numpick2 = int(input("PLAYER 1 : Choose the number between [1-9] : "))
            # if(numpick2 in possibleNum):
            #     modifyarray(numpick2,'O')
            #     possibleNum.remove(numpick2)
            #     whosturn += 1 
            #     break

    winner = Winner(gameBoard)
    if(winner != "N"):
        print("Game over! Thank you for playing \n\n")
        break

# print("Final Status of Game : ")
# printgameBoard()
# ------------------------------------------------------------------------------------------------------------------------------------------------