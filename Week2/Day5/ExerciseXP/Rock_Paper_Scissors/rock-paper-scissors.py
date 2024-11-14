# import game as g


# def get_user_menu_choice():
#     res = []
#     while True: 
#         print("\033[45m\033[1m>>>>>>ROCK-PAPER-SCISSORS<<<<<<\033[0m")
#         print("Menu:")
#         print("(g) Play a new game)")
#         print("(x) Show scores and exit")
#         word = input(">>>")
#         if word == 'x':
#             dico = {res[index]:res.count(res[index]) for index, i in enumerate(res)}
#             print(f"Vous avez quitter le programme score : {dico}")
#             return False
#         elif word =='g':
#             new_game = g.Game()
#             res += new_game.play()

# def main():
#     get_user_menu_choice()

# main()