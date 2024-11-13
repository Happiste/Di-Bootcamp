# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount

#     def __str__(self):
#         return f"{self.amount} {self.currency}"
    
#     def __int__(self): 
#         return self.amount
    
#     def __repr__(self):
#         return f"{self.amount} {self.currency}"

#     def __add__(self, num):
#         if isinstance(num, int):
#             result = self.amount + num
#         elif isinstance(num, Currency):
#             if num.currency == self.currency:
#                 result = self.amount + num.amount
#             else:
#                 raise Exception(f"TypeError cannot add between Currency type <dollars> and <shekel>")
#         return result   
 
#     def __iadd__(self, num):
#         if isinstance(num, int):
#             self.amount += num
#         elif isinstance(num, Currency):
#             if num.currency == self.currency:
#                 self.amount += num.amount
#             else:
#                 raise Exception(f"TypeError cannot add between Currency type <dollars> and <shekel>")
#         return self
        
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)

# print(str(c1))
# print(int(c1))
# print(c1 + 5)
# c1 += 20
# c1 += c2
# print(c1)


# # #Excercise 2 : Import > Check excercise_one and func.py

# #Excercise3: String Module

# import string
# import random
# lower_upper_alphabet = string.ascii_lowercase + string.ascii_uppercase


# print(random.sample(lower_upper_alphabet, 5))

# #Excecise 4 : Current Date

# import datetime as d
# now = d.datetime.now().replace(microsecond=0)


# print(now)

# #Excercise 5 Amount of time left until january 1st
# import datetime as d


# def time_left_until_first():
#     now = d.datetime.now().replace(microsecond=0)
#     first_january = d.datetime(2025, 1, 1, 00,00,00)
#     until_first = first_january - now
#     return f"The 1st January is in {until_first} hours"

# print(time_left_until_first())

# # #Excercise 6 Birthday and Minutes

# import datetime as d


# def how_much_time_in_minutes(birthday):
#     now = d.datetime.now().replace(microsecond=0)
#     my_birthday = d.datetime.strptime(birthday, "%Y, %m, %d, %H, %M, %S")
#     how_much = now - my_birthday
#     in_minutes = how_much.total_seconds() // 60
#     return f"you are a Human being for about {how_much} hours either {int(in_minutes)} minutes"

# print(how_much_time_in_minutes("1990, 2, 13, 6, 00, 00"))

#Excercise 7 Faker Module

# from faker import Faker

# users = []

# def add_users():
#     dict_user = {"name" : my_user.name(), "address" : my_user.address(), "langage code":my_user.language_code()}
#     users.append(dict_user)


# my_user = Faker()
# add_users()
# add_users()
# add_users()
# add_users()

# print(users)
