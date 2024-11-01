# #Exo 1 
# string = "Hello world\n"
# print(string*4)

# #Exo 2
# result = (99**3)*8
# print(result)

# #Exo 3 
# # 5 < 3 = False
# # 3 == 3 = True
# # 3 == "3" = False
# # "3" > 3 = False
# # "Hello" == "hello" = False

# #Exo 4
# brand_computer = "Macbook Pro, intel"
# print(f"i have a {brand_computer}  computer")

# #Exo 5
# name = "Jonathan"
# age = 34
# shoe_size = 44
# info = f"my name is {name}, and i'am {age} years old, oh and of course before i forget my shoes size is {shoe_size}"
# print(info)

# #Exo 6
# var_a = 13
# var_b = 5
# if var_a > var_b:
#     print("Hello World")

# #Exo 7
# print (f"please enter a number: ")
# while True:
#     try:
#         num = int(input())
#         if num % 2 == 0:
#             print("This number is even!")
#         else:
#             print("This number is odd!")
#         break
#     except ValueError:
#         print("You must enter an integer")

# #Exo 8
# my_name = "Jonathan"
# print("What is your name ?: ")
# your_name = input()
# if my_name == your_name:
#     print("WTF ! Like ME ! Jonathan 4the Win!")
# else: 
#     print("Your name is fucked")

#Exo 9
# authorized = 145
# print("what is height ?: ")
# while True:
#     try:
#         size_user = int(input())
#         if size_user >= authorized:
#             print("Okay good you are tall enough ! Have a nice ride !")
#         else:
#             print("you need to eat some soupe bro")
#         break
#     except ValueError:
#         print("You need to enter an number")

#EX GOLD
#Exo1

# hi_all = "\033[32mHello \033[0mworld\n"
# loving_python = "\033[32mI \033[0mlove Python\n"
# print(f"{hi_all}" * 4 + f"{loving_python}" * 4)

#Exo2

print("please enter a number between 1 and 12 (include)")
while True:
    try:
        ask_number = int(input())
        if ask_number >= 3 and ask_number <= 5:
            print("Spring's Time")
        elif ask_number >= 6 and ask_number <= 8:
            print("Summer's Time")
        elif ask_number >= 9 and ask_number <= 11:
            print("Autumn's Time")
        elif (ask_number >= 1 and ask_number <=2) or ask_number == 12:
            print("Winter is coming")
        else:
            print("You need to put a number between 1 and 12")
        break
    except ValueError:
        print("You need to put a number between 1 and 12 not a string")







