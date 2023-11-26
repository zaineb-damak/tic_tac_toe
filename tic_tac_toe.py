import random

board = [" " for i in range(9)]

player_turn =random.randint(0,1) # 0 for player, 1 for computer

turn_in_game = 0

player = "X"
computer = "O"

winning_combos = [  [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
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
    # Get the available moves on the board
    available_moves=[i for i in range(9) if board[i]==" "]
    # Initialize a list to store the count of available moves in each winning combination
    best_combos = []
    
    for combo in winning_combos:
        count=0
        # Count how many available moves are in the current winning combination
        for move in available_moves:
            if move in combo:
                count += 1
        best_combos.append([combo,count])

# Filter items with the second value greater than 0
    filtered_list = [item for item in best_combos if item[1] > 0]
    min_item = min(filtered_list, key= lambda x:x[1])
# Find all items with the minimum value in the second position
    min_items = [item for item in best_combos if item[1] == min_item[1]]

# If there are still available moves, choose the first move in the first winning combination with the minimum count
    if len(available_moves)>0:
        for move in available_moves:
            for item in min_items:
                if move in item[0]:
                    return move

def check_win(player_symbol):
    #check horizontal line
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
   draw_board()
  

    