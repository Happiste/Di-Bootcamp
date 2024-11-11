# import ExcerciceXP as f

# class TheIncredibles(f.Family):
#     def __init__(self, last_name, members):
#         super().__init__(last_name, members)
     
#     def use_power(self, name):
#         for person in self.members:
#             if super().is_18(name) and person["name"] == name:
#                 print(f"{name} is using is power to {person["power"]}")
#                 break
#         else: 
#             raise Exception(f"{name} n'a pas le droit d'utiliser ses pouvoir, il/elle n'a pas 18 ans ")
        
#     def incredible_presentation(self):
#         super().show_family()
#         print("         \033[31m/!\WARNING THIS IIS A INCREDIBLE FAMILY/!\ \033[0m")
#         for person in self.members:
#             print(f"{person['name']} >> Power: {person['power']} - Incredible Name: {person['incredible_name']}\n")
    
#     def super_born(self, **kwargs):
#         super().born(**kwargs)
                



# my_super_family = [
#     {'name':'GP','age':31,'gender':'Male','is_child':False, 'power': 'fly','incredible_name':'Gallery Du Papier paint'},
#     {'name':'Celine','age':32,'gender':'Female','is_child':False, 'power': 'read minds','incredible_name':'P\'tit pouce'}
#             ]

# super_bitane_family = TheIncredibles('Super Bitane', my_super_family)
# super_bitane_family.use_power('Celine')
# super_bitane_family.incredible_presentation()
# super_bitane_family.super_born(name='John', age = 2, gender = 'Male', is_child=True,power = 'super Stenght', incredible_name = 'Unknown Power')
# super_bitane_family.incredible_presentation()
