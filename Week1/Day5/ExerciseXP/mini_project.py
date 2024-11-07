#Mini Project 

lst = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def welcome_game():
    return(print("WELCOME TO TIC TAC TOE!"))

def display_board():
    
    print(f"{lst[0]} | {lst[1]} | {lst[2]}")
    print("---------")
    print(f"{lst[3]} | {lst[4]} | {lst[5]}")
    print("---------")
    print(f"{lst[6]} | {lst[7]} | {lst[8]}")
    return(lst)
#display_board()

def player_input(player):
    display_board()
    pos = (int(input(f"please chose en case between 1 and 9: " )) - 1)
    if lst[pos] == ' ':
        lst[pos] = player
        display_board()
    else:
        print("please chose an other case: ")

def check_win():
    win_conditions = [
        [lst[0], lst[1], lst[2]], 
        [lst[3], lst[4], lst[5]],
        [lst[6], lst[7], lst[8]],
        [lst[0], lst[3], lst[6]],
        [lst[1], lst[4], lst[7]],
        [lst[2], lst[5], lst[8]],
        [lst[0], lst[4], lst[8]],
        [lst[2], lst[4], lst[6]]
    ]
    
    for line in win_conditions:
        if line[0] == line[1] == line[2] != ' ':
            return True
    return False

def play():
    welcome_game()
    actual_player = "X"
    while True: 
        player_input(actual_player)
        if check_win():
            print(f"Congrats ! Player {actual_player} wins")
            break
        elif " " not in lst:
            print("No one wins !")
            break
        if actual_player == "X":
            actual_player = "O"
            print("\njoueur2: \n")
        else:
            print("\nJoueur1: \n")
            actual_player = "X"

play()