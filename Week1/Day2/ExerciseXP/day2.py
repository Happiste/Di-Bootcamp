#Exo1
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

#Exo 2
# we can't add some value to a tuple, the only way is to convert the tuple into a list add value, and re convert the list in tuples or you can concatenate 2 tuples. 
# my_tuples = (1,2,3)
# print(my_tuples)
# add_value = list(my_tuples)
# print(add_value)
# add_value.append(4)
# print(add_value)
# my_tuples = tuple(add_value)
# print(my_tuples)

#Exo 3

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

#Exo 4
# lst1 = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
# print(lst1)
# lst2 = [1.5 + 0.5 * i for i in range(8)]
# print(lst2)

#Exo 5
# for i in range(1,21):
#     print(i)

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

#Exo 6 
# my_name = "Jonathan"
# your_name =""
# while my_name != your_name:
#     your_name = input("what is your name ?: ")
    
#Exo 7

# fav_fruits = "banana kiwi blueberries" #input("what is your favorit fruits? :")
# lst_fruits = fav_fruits.split()
# ask = input("Chose a fruit please : ")
# if ask in lst_fruits:
#     print("You chose one of your favorite fruits! Enjoy!")
# else:
#     print("You chose a new fruit. I hope you enjoy")

#Exo 8 

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

#Exo 9 

price = 0
nb = int(input("how much are you ?"))
print(f"you are {nb}")
for nb in range(nb):
    age = int(input("how old are you ? "))
    print(f"your age is {age}")
    if age < 3:
        price = price + 0
        print(f"actual price : {price}")
    elif age >= 3 and age <= 12:
        price = price + 10
        print(f"actual price : {price}")
    elif age > 12:
        price = price + 15
        print(f"actual price : {price}")
print(f"total price: {price}")