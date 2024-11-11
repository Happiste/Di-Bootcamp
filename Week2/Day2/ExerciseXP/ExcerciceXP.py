# # #Exo 1

# # class Pets():
# #     def __init__(self, animals):
# #         self.animals = animals

# #     def walk(self):
# #         for animal in self.animals:
# #             print(animal.walk())

# # class Cat():
# #     is_lazy = True

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def walk(self):
# #         return f'{self.name} is just walking around'

# # class Bengal(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'

# # class Chartreux(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'
    
# # class Siamese(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'
    
# # buggy = Bengal("buggy", 1)
# # shanks = Chartreux("shanks", 5)
# # yuna = Siamese("Yuna", 3)
# # all_cats = [buggy, shanks, yuna]
# # sara_pets = Pets(all_cats)
# # sara_pets.walk()

# #Exo 2 Dogs

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight

#     def bark(self):
#         bark = f"{self.name} is barking"
#         return bark
    
#     def run_speed(self):
#         run_speed = int(self.weight/self.age*10)
#         return run_speed
    
#     def fight(self, other_dog):
#         if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
#             return f"{self.name} won the fight"
#         else:
#             return f"{other_dog.name} won the fight"

# my_dog = Dog("Taz", 3, 30)
# your_dog = Dog("happy", 10, 35)
# print(my_dog.bark())
# my_dog.run_speed()
# print(my_dog.fight(your_dog))


#excercice 4 Family

class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.kwargs = kwargs
        self.members.append(kwargs)
        print(f"Mazal Tov ! {kwargs["name"]} is born ! ")


    def is_18(self, name):
        for index, person in enumerate(self.members):
            if person["name"] == name and self.members[index]["age"] >= 18:
                print(f"{name} est majeur")
                return True
            elif person["name"] == name and self.members[index]["age"] < 18:
                print(f"{name} est mineur")
                return False
        else:
            print(f"{name} does not exist in this family")

    def show_family(self):
        print(f"              \033[34m{self.last_name.upper()}'s Family\033[0m")
        for index, person in enumerate(self.members):
            print(
f"""                 NAME: {person["name"]}
- AGE:{person["age"]} - GENDER: {person["gender"]} - IS CHILD?: {person["is_child"]}
""")



        

my_family = [
    {'name':'GP','age':31,'gender':'Male','is_child':False},
    {'name':'Celine','age':32,'gender':'Female','is_child':False}
]

famille_bitane = Family("Bitane", my_family)
famille_bitane.born(name="Jenny", age = 4, gender = "Female", is_child=True)
famille_bitane.born(name="John", age = 2, gender = "Male", is_child=True)
famille_bitane.born(name="MickMick", age = 0, gender = "Male", is_child=True)
famille_bitane.born(name="Trafik", age = 0, gender = "Male", is_child=True)
famille_bitane.show_family()
famille_bitane.is_18("John")
    

    

