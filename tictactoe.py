import random
## It is 
## display function of 
## a board
def display_board(board):
    print("   |     |")
    print(" "+board[8]+" |  "+board[7]+"  | "+board[6])
    print("   |     |")
    print("--------------")
    print("   |     |")
    print(" "+board[5]+" |  "+board[4]+"  | "+board[3])
    print("   |     |")
    print("--------------")
    print("   |     |")
    print(" "+board[2]+" |  "+board[1]+"  | "+board[0])
    print("   |     |")
## Toss
## Function    
def game_toss():
    toss=random.randint(1,2)
    if toss==1:
        return 'Player 1'
    else:
        return 'Player 2'
## Player selection between X and 0
def player_input():
    choice=" "
    while not (choice=="X" or choice=="O"):
        choice=input('Player 1: Do you want to be X or O? ').upper()
    if choice=="X":
        return ("X","O")
    else:
        return ("O","X")                   
##put on the game board
def put_board(board,marker,position):
    board[position]=marker
## win check
def win_check(board,marker):
    return ((board[0]==marker and board[1]==marker and board[2]==marker) or## For horizontal line
             (board[3]==marker and board[4]==marker and board[5]==marker) or#
             (board[6]==marker and board[7]==marker and board[8]==marker) or#
             (board[0]==marker and board[3]==marker and board[6]==marker) or## For verticle line
             (board[1]==marker and board[4]==marker and board[7]==marker) or#
             (board[2]==marker and board[5]==marker and board[8]==marker) or#
             (board[0]==marker and board[4]==marker and board[8]==marker) or## For diagnals
             (board[2]==marker and board[4]==marker and board[6]==marker))
## Checking space in blankls
def space_check(board,position):
    return board[position]==" "
## Board check
def board_full(board):
    for x in range(0,9):
        if space_check(board,x):
            return False
    return True        
## Playing the game
#again
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
##Player Choice for the next position
def player_choice(board):
    position = -1
    
    while position not in [0,1,2,3,4,5,6,7,8] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
##Main game
#logic
print('Welcome to tic tac toe')
while True:
    Board=[" "]*100##To clear screen
    player1_marker,player2_marker=player_input()
    chance=game_toss()
    print("{} will go first".format(chance))
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
         if chance=="Player 1":
             display_board(Board)
             position= player_choice(Board)
             put_board(Board, player1_marker, position)
             ##Checking winning condition
             if win_check(Board,player1_marker):
                 display_board(Board)
                 print("Congratulation!!{}have won this match".format(chance))
                 break
             else:
                 if board_full(Board):
                     display_board(Board)
                     print("Game is TIEEEEEEEEEEEEEEEEEE!!")
                     break      
                 else:
                     chance="Player 2"
         else:
             display_board(Board)
             position= player_choice(Board)
             put_board(Board, player2_marker, position)
             ##Checking winning condition
             if win_check(Board,player2_marker):
                 display_board(Board)
                 print("Congratulation!!{} won this match".format(chance))
                 break
             else:
                 if board_full(Board):
                     display_board(Board)
                     print("Game is TIEEEEEEEEEEEEEEEEEE!!")
                     break      
                 else:
                     chance="Player 1"            
    if not replay():
          break  