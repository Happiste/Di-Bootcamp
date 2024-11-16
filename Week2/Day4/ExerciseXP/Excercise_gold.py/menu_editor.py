# import menu_manager as m

# def load_manager():
#     return m.MenuManager()



# def show_user_manager(my_menu):
#     while True:
#         print("""
#                 MENU
#             (a) Add an item
#             (d) Delete an item
#             (v) View the menu
#             (x) Exit") """)
#         input_user = input(">>> ")
#         if input_user == 'a':
#             add_item_menu(my_menu)
#         elif input_user == 'd':
#             remove_item_menu(my_menu)
#         elif input_user == 'v':
#             show_restaurant_menu(my_menu)
#         elif input_user == 'x':
#             my_menu.save_to_file()
#             print("The menu has been saved !")
#             return False

# def add_item_menu(my_menu):
#     my_menu.add_item(input("please enter an item name: "), int(input("please enter an intem price: ")))
#     print("The new plate was successfuly added to the menu.")

# def remove_item_menu(my_menu):
#     my_menu.remove_item(input("please enter an item name: "))
#     print("The Plate was successfuly removed from the menu.")

# def show_restaurant_menu(my_menu):
#     my_menu.show_menu()


    
# def main():
#     my_menu = load_manager()
#     show_user_manager(my_menu)

# main()

