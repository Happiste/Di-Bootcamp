# # # # # # class Door:
# # # # # #     def __init__(self, is_opened):
# # # # # #         self.is_opened = is_opened

# # # # # #     def open_door(self):
# # # # # #         if not self.is_opened:
# # # # # #             self.is_opened = True
# # # # # #             print("I open the door")
# # # # # #         else:
# # # # # #             print("Door is already opened")

# # # # # #     def close_door(self):
# # # # # #         if self.is_opened:
# # # # # #             self.is_opened = False
# # # # # #             print("I close the Door")
# # # # # #         else:
# # # # # #             self.is_opened = True
# # # # # #             print("The Door is alteady closed")
    
# # # # # #     def show(self):
# # # # # #         if self.is_opened:
# # # # # #             print("The door is open")
# # # # # #         else:
# # # # # #             print("The door is close")

# # # # # # class BlockedDoor(Door):
# # # # # #     def open_door(self):
# # # # # #         raise Exception("Error: This door is blocked and cannot be opened.")

# # # # # #     def close_door(self):
# # # # # #         raise Exception("Error: This door is blocked and cannot be closed.")





# # # # # # my_door = Door(False)
# # # # # # my_door.show()
# # # # # # my_door.open_door()
# # # # # # my_door.show()
# # # # # # my_door.close_door()
# # # # # # my_door.show()
# # # # # # her_door = BlockedDoor(False)
# # # # # # her_door.open_door()

# # # # # class Computer():

# # # # #     def __init__(self):
# # # # #         self.name = "Apple Computer" # public
# # # # #         self.__max_price = 900 # private

# # # # #     def sell(self):            # public method
# # # # #         print(f"Selling Price: {self.__max_price}")

# # # # #     def __sell(self):          # private method
# # # # #       print('This is private method')

# # # # #     def set_max_price(self, price):
# # # # #         self.__max_price = price

# # # # # c = Computer()
# # # # # c.sell()

# # # # class Parrot():

# # # #     def fly(self):
# # # #         print("Parrot can fly")

# # # #     def swim(self):
# # # #         print("Parrot can't swim")

# # # # class Penguin():

# # # #     def fly(self):
# # # #         print("Penguin can't fly")

# # # #     def swim(self):
# # # #         print("Penguin can swim")

# # # # # common interface
# # # # def flying_test(bird):
# # # #     bird.fly()

# # # # def swimming_test(bird):
# # # #     bird.swim()

# # # # #instantiate objects
# # # # blu = Parrot()
# # # # peggy = Penguin()

# # # # # passing the object
# # # # flying_test(blu)
# # # # # >> Parrot can fly

# # # # flying_test(peggy)
# # # # swimming_test(blu)
# # # # # >> Penguin can't fly


# # # class A():

# # #     def dothis(self):
# # #         print("doing this in A")


# # # class B(A):
# # #     pass


# # # class C():
# # #     def dothis(self):
# # #         print("doing this in C")


# # # class D(C, B):
# # #     pass

# # # d_instance = D()
# # # d_instance.dothis() 

# # class Book():
# #     def __init__(self, title, author, publication_date, price):
# #         self.title = title
# #         self.author = author
# #         self.publication = publication_date
# #         self.price = price

# #     def present(self):
# #         print(f'Title: {self.title}')

# # class Fiction(Book):
# #     def __init__(self, title, author, publication_date, price, is_awesome):
# #         super().__init__(title, author, publication_date, price)
# #         self.genre = 'Fiction'
# #         self.is_awesome = is_awesome
# #         if self.is_awesome:
# #             self.bored = False
# #             print('Woow this is an awesome book')
# #         else:
# #             self.bored = True
# #             print('I am very bored')

# # if __name__ == '__main__':
# #     foundation = Fiction('Asimov', 'Foundation', '1966', '5£', True)
# #     foundation.present()
# #     print(foundation.price)
# #     print(foundation.bored)
# #     boring_book = Fiction('boring_guy', 'boring_title', 'boring_date', '9000£', False)
# #     print(boring_book.bored)

# valid_flag = False
# while not valid_flag:
#     userage = input("How old are you?")
#     try:
#         userage    = int(userage)
#         valid_flag = True
#     except:
#         print("please enter a real age")
# print("Next year, your age will be",userage+1)
valid_flag = False
while not valid_flag:
    userage = input("How old are you?")
    try:    # TRY THIS
        userage    = int(userage)
    except: # IF YOU GOT AN ERROR
        print("Wrong age!")
    else:   # ELSE
        valid_flag = True
    finally:
        print('There may or may not have been an exception.')

print("Next year, your age will be",userage+1)
 