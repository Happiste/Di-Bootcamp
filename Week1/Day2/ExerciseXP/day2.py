# Exo1
# my_fav_num = {13, 14, 15}
# print(my_fav_num)
# my_fav_num.add(2)
# my_fav_num.add(5)
# print(my_fav_num)
# my_fav_num.remove(2)
# print(my_fav_num)
# friend_num ={5, 10, 4}
# print(friend_num)
# our_fav_num = my_fav_num.union(friend_num)
# print(our_fav_num)

# Exo 2
# we can't add some value to a tuple, the only way is to convert the tuple into a list add value, and re convert the list in tuples or you can concatenate 2 tuples. 
# my_tuples = (1,2,3)
# print(my_tuples)
# add_value = list(my_tuples)
# print(add_value)
# add_value.append(4)
# print(add_value)
# my_tuples = tuple(add_value)
# print(my_tuples)

# Exo 3

# basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# print(basket)
# basket.remove("Banana")
# print(basket)
# basket.remove("Blueberries")
# print(basket)
# basket.append("kiwi")
# print(basket)
# basket.insert(0, "Apples")
# print(basket)
# print(basket.count("Apples"))
# basket.clear()
# print(basket)

# Exo 4
# lst1 = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(lst1)
# lst2 = [1.5 + 0.5 * i for i in range(8)]
# print(lst2)

# Exo 5
# for i in range(1,21):
#     print(i)

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# Exo 6 
# my_name = "Jonathan"
# your_name =""
# while my_name != your_name:
#     your_name = input("what is your name ?: ")
    
# Exo 7

# fav_fruits = "banana kiwi blueberries" #input("what is your favorit fruits? :")
# lst_fruits = fav_fruits.split()
# ask = input("Chose a fruit please : ")
# if ask in lst_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

# Exo 8 

# ask_topping = ""
# lst_toppings = []
# while ask_topping != "quit":
#     ask_topping = input("\033[31mWhat toppings can i add to your pizza ? ")
#     if ask_topping != "quit":
#         if ask_topping == '' or ask_topping == ' ':
#             print("this is not a topping")
#             continue
#         lst_toppings.append(ask_topping)
#         print(f"\033[32mOkay i add {ask_topping} to your pizza")
# toppings = ", ".join(lst_toppings)
# total_price = 10 + 2.5 * len(lst_toppings)
# print(f"\033[0mYou choose to add {toppings} to your pizza, the price is 10$ for the base and 2,5$ for each topping: {total_price}")

# #Exo 9 - 1, 2, 3

# price = 0
# nb = int(input("how much are you ?"))
# print(f"you are {nb}")
# for nb in range(nb):
#     age = int(input("how old are you ? "))
#     print(f"your age is {age}")
#     if age < 3:
#         price = price + 0
#         print(f"actual price : {price}")
#     elif age >= 3 and age <= 12:
#         price = price + 10
#         print(f"actual price : {price}")
#     elif age > 12:
#         price = price + 15
#         print(f"actual price : {price}")
# print(f"total price: {price}")

# #Exo 9 - 4
# list_name = ["John", "Yaël", "Benjaminn", "David"]
# final_lst = []
# for nb in list_name:
#     age = int(input(f"what is your age {nb}: "))
#     if 16 <= age <= 21:
#         final_lst.append(nb)
#     else:
#         continue
# print(final_lst)

# #Exo 10

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
# print(f"la commande: {sandwich_orders}")
# finished_sandwiches = []
# for sandwich in sandwich_orders[:]:
#     if sandwich != "Pastrami sandwich":
#         print(f"I made your {sandwich} sandwich")
#         finished_sandwiches.append(sandwich)
#         sandwich_orders.remove(sandwich)
#     else:
#         print(f"je supprime : {sandwich}")
#         sandwich_orders.remove(sandwich)
# print(f"Ce qu'il reste de la commande: {sandwich_orders}\nCe qui a été préparer de la commande: {finished_sandwiches}")

# #XP GOLD 
# #Exo 1
# lst1 =[1, 2 , 3 ,4, 5]
# lst2 = ["John", "Yaël"]
# lst1.extend(lst2)
# print(lst1)

# #Exo 2

# for x in range(1500, 2500):
#     if x % 5 == 0 and x % 7 == 0:
#         print(x)

# #Exo 3
# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# ask = input("entrée un prénom:")
# if ask in names:
#     index = names.index(ask)
#     print(index)

# #Exo 4
# print("Test Data")
# lst = []
# for i in range(1,4):
#     a = int(input(f"Input the {i} number: "))
#     lst.append(a)
# bigger_num = max(lst)
# print(f"the greatest number is {bigger_num}")

# #Exo 5
# letters = "abcdefghijklmnopqrstuvwxyz"
# vowels = "aeiouy"
# for letter in letters:
#     if letter in vowels:
#         print(f"{letter} is a vowels")
#     else:
#         print(f"{letter} is consonant")

# #Exo 6
# #computer mouse keyborad screen python code developperwords = []
# ask_word = input("you need to write 7 words separate by a space please: ")
# words = ask_word.split()
# ask_letter = input("you need to write a letter: ")
# for word in words:
#     if ask_letter in word:
#         print(f"\033[0mThere is the index searched in the word: {word.index(ask_letter)}")
#     else:
#         print(f"\033[31mWe can't find: {ask_letter}, in the word: {word}")

# #Exo 7
# lst = range(1, 100000000)
# print(lst)
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# #Exo 8
# lst = []
# tpl = {}
# ask_num = input("please enter as many numbers as you want separate by a comma: ")
# lst = ask_num.split(",")
# tpl = tuple(lst)
# print(lst)
# print(tpl)

# Exo 9 

# import random as r
# random_num = r.randrange(1,10)
# print(random_num)
# attempt = 0
# while True:
#     try:
#         ask_number = input("please enter a number from 1 to 9 (including)")
#         attempt += 1
#         if ask_number == "quit":
#             break
#         else:
#             attempt = attempt + 1
#             ask_num = int(ask_number)
#             if 0 < ask_num < 10:
#                 if ask_num == random_num:
#                     print(f"Good Guess ! Your number: {ask_num}, the random number: {random_num} you found the correnct number in {int(attempt/2)} attempts")
#                     break
#                 else:
#                     continue
#             else:
#                 print(f"please enter a number between 1 and 9 inclusive {ask_num} is not between")
#                 continue
#     except ValueError:
#         print("Value Error: invalid value, you need to put a integer not a string.")

# #XP NINJA

# #Exo 1
c = 50
h = 30
d = "100,150,180"#input("please enter many numbers as you want separate by a comma: ")
lst = d.split(',')
store = []
str_result=""
print(lst)
for num in lst:
    result = ((2*c*int(num))/h) ** 0.5
    str_result += str(int(result)) + ","
    # store.append(int(result))
print(str_result.rstrip(','))


