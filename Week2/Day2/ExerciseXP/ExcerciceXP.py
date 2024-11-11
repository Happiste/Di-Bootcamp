# #Exo 1

# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# buggy = Bengal("buggy", 1)
# shanks = Chartreux("shanks", 5)
# yuna = Siamese("Yuna", 3)
# all_cats = [buggy, shanks, yuna]
# sara_pets = Pets(all_cats)
# sara_pets.walk()

#Exo 2 Dogs

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        bark = f"{self.name} is barking"
        return bark
    
    def run_speed(self):
        run_speed = int(self.weight/self.age*10)
        return run_speed
    
    def fight(self, other_dog):
        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return f"{self.name} won the fight"
        else:
            return f"{other_dog.name} won the fight"

my_dog = Dog("Taz", 3, 30)
your_dog = Dog("happy", 10, 35)
print(my_dog.bark())
my_dog.run_speed()
print(my_dog.fight(your_dog))




