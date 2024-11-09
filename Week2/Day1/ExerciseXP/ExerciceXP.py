# #EXO 1
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age

# shanks = Cat("shanks", 5)
# Buggy = Cat("Buggy", 1)
# Yuna = Cat("Yuna", 3)

# def oldest_cat(*cats):
#     oldest_cat = cats[0]
#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return(oldest_cat)

# oldest = oldest_cat(shanks, Buggy, Yuna)
# print(oldest.name, oldest.age)

# #Exo 2
 
# class Dog:
#     def __init__(self, name, height, owner):
#         self.name = name
#         self.height = height
#         self.owner = owner

#     def bark(self):
#         print(f"{self.name} goes woof!")

#     def jump(self):
#         x = self.height * 2
#         print(f"{self.name} jumps {x} cm height ")
    
#     def details_dog(self):
#         print(f"The name of {self.owner}'s dog is {self.name} and is height is {self.height}!")

# def whos_bigger(*dogs):
#     bigger = dogs[0]
#     for dog in dogs:
#         if dog.height > bigger.height:
#             bigger = dog
#     return bigger



# davids_dog = Dog("Happy", 60, "David")
# davids_dog.details_dog()
# davids_dog.bark()
# davids_dog.jump()

# sarahs_dog = Dog("Teacup", 20, 'Sarah')
# sarahs_dog.details_dog()
# sarahs_dog.bark()
# sarahs_dog.jump()

# my_dog = Dog("Taz", 66, "John")
# my_dog.details_dog
# my_dog.bark()
# my_dog.jump()

# biggest = whos_bigger(davids_dog, sarahs_dog, my_dog)
# print(f"the biggest dog is {biggest.owner}'s dog: {biggest.name}")

# #Exo 3
# class Song:
#     def __init__(self, lst_lyrics):
#         self.lst_lyrics = lst_lyrics

#     def sing_me_a_song(self):
#         for line in self.lst_lyrics:
#             print(line)

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

# stairway.sing_me_a_song()

# #Exo 4
# class Zoo:
#     def __init__(self, zoo_name):
#         self.zoo_name = zoo_name
#         self.animals = []

#     def add_animal(self, new_animal):
#         if new_animal in self.animals:
#             print("we already have this animals")
#         else:
#             self.animals.append(new_animal)
#             print(f"A new animal: {new_animal} has join the family of {self.zoo_name}  ")

#     def get_animals(self):
#         print(f"This Zoo is called: {self.zoo_name} and has: {self.animals} animals")

#     def sell_animal(self, animal_sold):
#         if animal_sold in self.animals:
#             self.animals.remove(animal_sold)
#             print(f"the {animal_sold} has been sold")
#         else:
#             print("we can't sell what we don't have ! ")

#     def sorted_animals(self):
#         animal_sorted = sorted(self.animals)
#         dico = {} 
#         for animal in animal_sorted:
#             first_letter = animal[0]
#             if first_letter not in dico:
#                 dico[first_letter] = []
#             dico[first_letter].append(animal) 
#         grouped_animals = {}
#         group_number = 1
#         for letter in dico:
#             grouped_animals[group_number] = dico[letter]
#             group_number +=1
#         return(grouped_animals)
  
                
#     def get_groups(self):
#         sorted = self.sorted_animals()
#         print(f"here is the grouped animals: {sorted}")

                           

# my_zoo = Zoo("John's Zoo")
# my_zoo.add_animal("Tiger")
# my_zoo.add_animal("Lion")
# my_zoo.get_animals()
# my_zoo.sell_animal("Lion")
# my_zoo.get_animals()
# my_zoo.add_animal("Tiger")
# my_zoo.add_animal("Lion")
# my_zoo.add_animal("Levrier")
# my_zoo.sell_animal("Cheval")
# my_zoo.add_animal("Horse")
# my_zoo.get_animals()
# my_zoo.sorted_animals()
# my_zoo.get_groups()

