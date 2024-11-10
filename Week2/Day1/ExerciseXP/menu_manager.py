#Exo 3 restaurant Mennu Manager

class MenueManager:
    def __init__(self):
        self.menu = [
            {"name" : "Soup", "price" : 10, "spice" : "B", "gluten" : False},
            {"name" : "Hamburger", "price" : 15, "spice" : "A", "gluten" : True},
            {"name" : "Salad", "price" : 18, "spice" : "A", "gluten" : False},
            {"name" : "French Fries", "price" : 5, "spice" : "C", "gluten" : False},
            {"name" : "Beef bourguignon", "price" : 25, "spice" : "B", "gluten" : True}
        ]

    def add_items(self, name, price, spice, gluten):
        for line in self.menu:
            if name == line["name"]:
                print("we already have this dish in the menue")
                return
        new_dish = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_dish)
      

    def update_item(self, name, price, spice, gluten):
        for line in self.menu:
            if line["name"] == name:
                line["price"] = price
                line["spice"] = spice
                line["spice"] = gluten
                break
        else:
            print(f"{name} dish does not exist in the menu")

    def remove_item(self,name):
        for index, line in enumerate(self.menu):
            if line["name"] == name:
                self.menu.pop(index)
        else:
            print("We can't remove a dish we don't have")
                
    def get_menu(self):
        for i in self.menu:
            print(i)
        print("------------")
       
my_menu = MenueManager()
my_menu.get_menu()
my_menu.add_items("Shawarma", 12, "C", True)
my_menu.get_menu()
my_menu.add_items("Shawarma", 12, "C", True)
my_menu.get_menu()
my_menu.update_item("Soup", 55, "C", False)
my_menu.get_menu()
my_menu.update_item("Massala", 55, "C", False)
my_menu.get_menu()
my_menu.add_items("Shawarma", 12, "C", True)
my_menu.get_menu()
my_menu.remove_item("Soup")
my_menu.get_menu()
my_menu.remove_item("Soup")
my_menu.get_menu()



