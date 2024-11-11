# #Exo 3 Dogs Domesticated

# import ExcerciceXP as x
# import random as r

# class PetDog(x.Dog):
#     def __init__(self, name, age, weight):
#         super().__init__(name, age, weight)
#         self.trained = False

#     def train(self):
#         print(self.bark())
#         self.trained = True

#     def play(self, *args):
#         dogs = ""
#         for arg in args:
#             dogs += " " + arg.name
#         dog_names = self.name + dogs
#         print(f"{dog_names} all play together")

#     def do_a_trick(self):
#         lst_action = [" does a barrel roll", " stand on his back legs", " shake your hand", " plays dead"]
#         action = r.choice(lst_action)
#         if self.trained == True:
#             print(f"{self.name}{action}")
#         else: 
#             print(f"your dog {self.name} is not trained yet he just can bark")
            
            


        


# his_dog = PetDog("Edouard", 8, 35)
# his_dog.train()
# his_dog.play(x.my_dog, x.your_dog)
# his_dog.do_a_trick()
