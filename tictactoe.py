#compiled by Ess 

from random import choice 
from time   import sleep  

print("********THE GAME IS ABOUT TO START********")
print("------")


def Welcome():
    print('   ****Welcome to Tic_Tac_Toe game 😍****')
    
    sleep(1)
    print()
    print('Computer decides who plays first')
    print()
    #for Hint
    print('If you need Hint press[H,h]')
    sleep(1)
    print()
    print('''      ******* Format of Game ******
          |    |         1 | 2 | 3
       - - - - - -      - - - - - - 
          |    |         4 | 5 | 6
       - - - - - -      - - - - - - 
          |    |         7 | 8 | 9
                                           ''')


#Fuction to draw Board
def DrawBoard(board,NeedSleep=True):
    
    if NeedSleep:
        sleep(1)
    print()
    print('             '+board[1]+'  |  '+board[2]+'  |  '+board[3])
    print('             - - - - - - - ')
    print('             '+board[4]+'  |  '+board[5]+'  |  '+board[6])
    print('             - - - - - - - ')
    print('             '+board[7]+'  |  '+board[8]+'  |  '+board[9])
    print()

#asking the player to choose  Letter  (X or O)
def InputPlayerLetter():
    letter=''
    #Ask until user enters x or o
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O')
        letter = input().upper()
     
    #returning list for later use
    if letter == 'X':
      return ['X','O']
    if letter == 'O':
      return ['O','X']

#Deciding who should play first randomly either computer or player
def WhoFirst():
    opponents = ['computer','player']
    if choice(opponents) == 'computer':
        return 'computer'
    else :
        return 'player'
        
#this function asks player to play again
def PlayAgain():
    print()
    print('Do you want to Play Again (y or n)')
    playagain = input().lower().startswith('y')
    return playagain

#function for making move
def MakeMove(board,letter,move):
    board[move] = letter

#check if any one win,returns True if wins
#horizontal => 3 | vertical => 3 | diagonal => 2
def IsWinner(board,letter):
    return ( (board[7] == letter and board[8] == letter and board[9] == letter ) or
             (board[4] == letter and board[5] == letter and board[6] == letter ) or
             (board[1] == letter and board[2] == letter and board[3] == letter ) or
             (board[1] == letter and board[4] == letter and board[7] == letter ) or
             (board[2] == letter and board[5] == letter and board[8] == letter ) or
             (board[3] == letter and board[6] == letter and board[9] == letter ) or
             (board[1] == letter and board[5] == letter and board[9] == letter ) or
             (board[3] == letter and board[5] == letter and board[7] == letter )  )

#duplicate board is useful when we wanted to make temporary changes to the temporary copy of the board without changing the original board
def GetBoardCopy(board):
    DupeBoard = []
    for i in board:
        DupeBoard.append(i)
    return DupeBoard
    
#fuction to check is space is free
def IsSpaceFree(board,move):
    return board[move] == ' '

#Getting the player move
def GetPlayerMove(board):
    move = ''
 
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not IsSpaceFree(board,int(move)):
        print()
        print('Enter your move (1 - 9)')
        move = input()
        #if player wants Hint
        if move in HintInput:
            return move
            break  
    return int(move)

#choose random move from given list
#it is used when AI  wants to choose out of many possibilities
def ChooseRandomFromList(board,MoveList):
    PossibleMoves = []
    for i in MoveList:
        if IsSpaceFree(board,i):
            PossibleMoves.append(i)
    if len(PossibleMoves) != 0:
        return choice(PossibleMoves)
    else:
        return None

#--------------------------------------
#Get computer move
def GetComputerMove(board,ComputerLetter):
    if ComputerLetter == 'X':
        PlayerLetter = 'O'    
    else:
       PlayerLetter = 'X'

    #1.check computer can win in next move
    for i in range(1,10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy,i):
            MakeMove(copy,ComputerLetter,i)
            if IsWinner(copy,ComputerLetter):
                return i


    #2.check player can win in next move
    for i in range(1,10):
        copy = GetBoardCopy(board)
        if IsSpaceFree(copy,i):
            MakeMove(copy,PlayerLetter,i)
            if IsWinner(copy,PlayerLetter):
                return i

    #3.checking for corner
    move = ChooseRandomFromList(board,[1,3,7,9])
    if move != None:
        return move
        
    #4.checking for the center
    if IsSpaceFree(board,5):
        return 5
        
    #5.checking for sides
    return ChooseRandomFromList(board,[2,4,6,8])
    
#---------------------------------------   

#checking board is full or not
def IsBoardFull(board):
    for i in range(1,10):
        if IsSpaceFree(board,i):
            return False
    return True
            
#fuction to print  the final win or tie board
#made this to separate usual board and winning or tie board
def FinalBoard(board,NeedSleep=True):
    print('            |-------------|')
    DrawBoard(board,NeedSleep)
    print('            |-------------|')

                    
#LETS START THE GAME
Welcome()
while True:
    #intialising board
    TheBoard = [' '] * 10
    PlayerLetter,ComputerLetter = InputPlayerLetter()
    turn = WhoFirst()
    print(f'The {turn} will go first')
    
    #gameloop
    Playing = True
    while Playing:
        
        if turn == 'player':
            print(f"    Turn => {turn}") 
            HintInput = ['Hint','hint','H','h'] 
            #taking players input
            move = GetPlayerMove(TheBoard)
            #if player needs Hint
            while move in HintInput:                
                #following code gives hint to the user
                #it runs player letter to computer AI
                HintBox = []
                for i in TheBoard:
                    HintBox.append(i)
                hint = GetComputerMove(HintBox,PlayerLetter)
                MakeMove(HintBox,PlayerLetter,hint)
                print(f'HINT : placing at {hint} is better')
                FinalBoard(HintBox,False)
                move = GetPlayerMove(TheBoard)
              
            MakeMove(TheBoard,PlayerLetter,move)
            
            
            if IsWinner(TheBoard,PlayerLetter):
                FinalBoard(TheBoard)                
                print('That was a nice trial ❣️')
                Playing = not Playing
            elif IsBoardFull(TheBoard):
                FinalBoard(TheBoard)
                print('The game is a TIE 😂')
                Playing = not Playing
            else :
                DrawBoard(TheBoard)
                turn = 'computer'
 
        else :
            #computer move
            print(f"    Turn => {turn}")
            move = GetComputerMove(TheBoard,ComputerLetter)
            MakeMove(TheBoard,ComputerLetter,move)
            
            
            if IsWinner(TheBoard,ComputerLetter):
                FinalBoard(TheBoard)
                print('That was a nice trial❣️')
                Playing = not Playing
            elif IsBoardFull(TheBoard):
                FinalBoard(TheBoard)
                print('The game is a TIE 😂')
                Playing = not Playing
            else :
                DrawBoard(TheBoard)
                turn = 'player'

    if not PlayAgain():
        print("********Well done.Keep Pythoning.. 🙌😍********")
        break
