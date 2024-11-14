# import random as r

# class Game:
#     def __init__(self):
#         self.user_item = ""
#         self.computer_item = ""
#         self.lst = ["paper", "rock", "scissors"]
        
#     def get_user_item(self):
#         while self.user_item not in self.lst:
#             self.user_item = input("Please enter paper, rock or scissors: ")
#         return self.user_item
        

#     def get_computer_item(self):
#         self.computer_item = r.choice(self.lst)
#         return self.computer_item

#     def get_game_result(self, user_item, computer_item):
#         user_item = self.get_user_item()
#         computer_item = self.get_computer_item()
#         if user_item == "paper" and computer_item == "rock":
#             return "win"
#         elif user_item == "rock" and computer_item == "scissors":
#             return "win"
#         elif user_item == "scissors" and computer_item == "paper":
#             return "win"
#         elif user_item == computer_item:
#             return "draw"
#         else:
#             return "loss"

        
#     def play(self):
#         result = self.get_game_result("", "")
#         lst_result = []
#         lst_result.append(result)
#         print(f"vous avez choisis : {self.user_item}")
#         print(f"the Computer: chose {self.computer_item}")
#         print(f"you {result}")
#         return lst_result
        
        


# if __name__ == '__main__':
#     game_one = Game()
#     game_one.play()

