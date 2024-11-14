# #Charactere Game

# class Character:
#     def __init__(self, name, life=20, attack =10):
#         self.name = name
#         self.life = life
#         self.attack = attack

#     def basic_attack(self, another_character):
#         if isinstance(another_character, Character):
#             another_character.life -= self.attack
#             print(f"{self.name} attack {another_character.name} et lui inflige {self.attack} de dégats!!")
#             return another_character.life
        
#     def show_life(self):
#         return f"Votre vie: {self.life}"
    
# class Druid(Character):
#     def __init__(self, name, life=20, attack=10):
#         super().__init__(name, life, attack)
#         print(f"A new Druid has been created: {self.name}") 

#     def meditate(self):
#         self.life += 20
#         print(f"The life of {self.name} increase by 20 ")
#         self.attack -= 2
#         print(f"The attack of {self.name} drop by 2")

#     def animal_help(self):
#         self.attack += 5
#         print(f"The Attack of {self.name} increase by 5")

#     def fight(self, other_character):
#         if isinstance(other_character, Character):
#             attack = (0.75*self.life + 0.75*self.attack)
#             other_character.life -= attack
#             print(f"{self.name} attack {other_character.name} et lui inflige {attack} de dégats!!")

# class Warrior(Character):
#     def __init__(self, name, life=20, attack=10):
#         super().__init__(name, life, attack)
#         print(f"A new Warrior has been created: {self.name}") 

#     def brawl(self, other_character):
#         if isinstance(other_character, Character):
#             other_character.life -= (2*self.attack)
#             self.life += 0.5*self.attack
#             print(f"{}")
        

    

# # john = Character("John")
# # yael = Character("Yaël")
# # print(yael.show_life())
# # john.basic_attack(yael)
# # print(yael.show_life())
        

# john = Druid("John")
# john.meditate()
# print(john.show_life())
# john.animal_help()
# print(john.attack)
# # yael = Druid("Yaël")
# # john.fight(yael)


