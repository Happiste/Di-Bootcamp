#Excercice XP GOLD 

#Exo 1

#perimetre = 2*pi*rayon
#air = pi*(radius**2)
import math 

class Circle:
    def __init__(self, radius=1.0):
        self.radius = radius

    def get_perimeter(self):
        perimeter = 2*math.pi*self.radius
        return(perimeter)
    
    def get_area(self):
        area = math.pi*(self.radius**2)
        return(area)
    
    def get_def(self):
        p = self.get_perimeter()
        a = self.get_area()
        print(f"un cercle de rayon {self.radius} à un perimétre de {round(p)} cm, et une aire de {round(a)}cm carrée")

my_circle = Circle(5.0)
my_circle.get_perimeter()
my_circle.get_area()
my_circle.get_def()


#Exo 2
import random as r

class Mylist:
    def __init__(self, lst):
        self.lst = lst

    def reversed_lst(self):
        list_reversed = self.lst[::-1]
        return(list_reversed)
    
    def sorted_list(self):
        sorted_list = sorted(self.lst)
        return(sorted_list)
    
    def copy_len_list(self):
        copy_list = [r.randint(1, 10000) for _ in range(len(self.lst))]
        print(f"here is the lenght copy list with random numbers : {copy_list}")
        return(copy_list)
    
    def get_list(self):
        print(f"""liste d'origine: {self.lst}
liste reversed: {self.reversed_lst()}
liste sorted : {self.sorted_list()}
the len copied list with random num: {self.copy_len_list()}""")

    
lst = [5,12,7,78,1,87,13,6]
my_list = Mylist(lst)
my_list.reversed_lst()
my_list.sorted_list()
my_list.get_list()
my_list.copy_len_list




