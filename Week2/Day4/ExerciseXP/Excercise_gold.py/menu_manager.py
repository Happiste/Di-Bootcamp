import json


class MenuManager:
    def __init__(self):
        with open("restaurant_menu.json", "r+") as f_obj:
            self.file =  json.load(f_obj)

    def add_item(self, new_item, price):
            if isinstance(new_item, str) and isinstance(price, float) or isinstance(price, int):
                new_item = {"name":new_item, 'price': price}
                self.file['items'].append(new_item)
                return self.file
            else:
                print("Please enter a real item and a real price.")
            
    
    def remove_item(self, rm_item):
        for item in self.file['items']:
            if item["name"] == rm_item:
                self.file['items'].remove(item)
                return self.file
        else:
            print("This item does not exist in the menu.")
    
    def save_to_file(self):
        file ='restaurant_menu.json'
        with open(file,'w') as f_obj:
           json.dump(self.file, f_obj, indent =2, sort_keys=True)
      


    def show_menu(self):
        count = 1
        for item in self.file['items']:
            print (f"Plate n{count}: {item['name']} • {item['price']}")
            count +=1

    
if __name__=='__main__':
    my_menu = MenuManager()
  
    my_menu.add_item("Pizza Napolitana" , 65)
    print(my_menu.show_menu())
    my_menu.remove_item('Vegetable soup')
    print(my_menu.show_menu())


