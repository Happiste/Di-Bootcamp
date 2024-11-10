#DailyChallenge

class Farm:
    def __init__(self, name_farm):
        self.name_farm = name_farm
        self.farm = {}
        self.type_animals = []
        
    
    def add_animals(self, animal, num=1):
        if animal not in self.farm:
            self.farm[animal] = num
            print(f"{num} {animal} have been add to the {self.name_farm} farm")
        else:
            self.farm[animal] += num
            print(f"{num} {animal} have been add to the existant herd")
    
    def get_info(self):
        print(f"{self.name_farm}'s farms")
        for animal, num in self.farm.items():
            print(f"{animal} : {num}\n")
        print("    E-I-E-I-0!")

    def get_animal_types(self):
        self.type_animals = [animal for animal in self.farm]    
        print(self.type_animals)
        return self.type_animals    
    
    def get_short_info(self):
       animal_types = ", ".join(self.get_animal_types())
       return f"{self.name_farm}'s farm has {animal_types}"

        



macdonald = Farm("McDonald")
macdonald.add_animals("cow", 23)
macdonald.add_animals("sheep", 5)
macdonald.add_animals("sheep")
macdonald.add_animals("chicken")
macdonald.add_animals("goat", 12)
macdonald.add_animals("cow", 5)
macdonald.get_info()
macdonald.get_animal_types()
macdonald.get_short_info()

    