import random

board = [" " for i in range(9)]

player_turn =random.randint(0,1) # 0 for player, 1 for computer
#player_turn = 0
turn_in_game = 0

player = "X"
computer = "O"

winning_combo = [  [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

def draw_board():
    for row in range(3):
        print("|".join(board[row * 3:row * 3 + 3]))
        
        
def game_play(player_turn, turn_in_game):
    while True:
        if turn_in_game > 8 :
            print("it's a tie")
            break

        draw_board()
        if player_turn== 1:
            print("computer's move")
            board[computer_move()]=computer
            if check_win(computer):
                print('computer won')
                break
            player_turn=0
            turn_in_game += 1
            continue
        else:
            try:
                move = int(input("enter a number from 1 to 9 \n")) - 1
            except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                continue
            if move<0 or move>8:
                print("number out of range. try again")
                continue
            if board[move] == " ":
                board[move]=player
                if check_win(player):
                    print("you won")
                    break
                player_turn=1
                turn_in_game += 1
                continue
            else:
                print("that box is already marked. try again")

def computer_move():
    available_moves=[i for i in range(9) if board[i]==" "]
    if len(available_moves)>0:
        return random.choice(available_moves)

def check_win(player_symbol):
    # score=0
    # for combo in winning_combo:
    #     print(combo)
    #     for index in combo:
    #         if board[index] == player_symbol:
    #             score += 1
    #             print(score)
    #         else:
    #             break
    #         if score == 3:
    #             return True
    # check horizontal line
    for i in range(0,9,3):
        if board[i] ==  board[i+1] == board[i+2] ==player_symbol:
            return True
    #check vertical line
    for i in range(3):
         if board[i] ==  board[i+3] == board[i+6] ==player_symbol:
             return True
    #check diagonal 
    if board[0] == board[4] == board[8] == player_symbol or board[2] == board[4] == board[6] == player_symbol:
        return True
    
    return False



if __name__ == "__main__":
   game_play(player_turn, turn_in_game)
  

    