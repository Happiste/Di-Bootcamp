# #Exo 1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dico = dict(zip(keys, values))
# print(dico)

#Exo 2
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8, 'john': 35}
# price = 0
# for (name, age) in family.items():
#     if age < 3:
#         pass
#     elif 3 <= age <= 12:
#         price += 10
#     else: 
#         price +=15
# print(price)

# #With input
# ask_name = []
# ask_age = []
# price = 0
# for i in range(1, (int(input("how much are you in your familly: ")))+1):
#     ask_name.append(input("please enter your name: "))
#     ask_age.append(int(input("please enter your age: ")))
#     dico = dict(zip(ask_name, ask_age))
#     for (name, age) in dico.items():
#      if age < 3:
#         pass
#      elif 3 <= age <= 12:
#         price += 10
#     else: 
#         price +=15

# print(price)

# #Exo 3
# dict_brand = {
#     "name":"Zara",
#     "creation_date":1975,
#     "creator_name":"Amancio Ortega Gaona",
#     "type_of_clothes": ['men', 'women', 'children', 'home'],
#     "international_competitors": ['Gap', 'H&M', 'Benetton'],
#     "number_stores":7000,
#     "major_color":{
#         "France":"blue",
#         "Spain":"red",
#         "US":['pink', 'green']
#     }
# }
# print(dict_brand)
# dict_brand['number_stores'] = 2
# print(dict_brand)
# client = ", ".join(dict_brand["type_of_clothes"])
# print(f"Zara's client include {client}")
# dict_brand.update({"country_creation":"Spain"})
# print(dict_brand)
# if dict_brand['international_competitors']:
#     dict_brand["international_competitors"].append("Desigual")
# print(dict_brand)
# del dict_brand["creation_date"]
# print(dict_brand)
# print(dict_brand["international_competitors"][-1])
# major_color = " and ".join(dict_brand["major_color"]["US"])
# print(f"the major clothes in the US are {major_color} ")
# print(len(dict_brand))
# for (key, value) in dict_brand.items():
#     print(key)

# more_on_zara = {}
# more_on_zara["creation_date"] = 1975 
# more_on_zara["number_stores"] = 10000 
# print(more_on_zara)
# dict_brand.update(more_on_zara)
# print(dict_brand)

# #exo 4

# #1/

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# user_dict = {user: count for count, user in enumerate(users)}
# print(user_dict)

# #2

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# user_dict = {count: user for count, user in enumerate(users)}
# print(user_dict)

#3

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# user_dict = {user: count for count, user in enumerate(users)}
# sorted = dict(sorted(user_dict.items()))
# print(sorted)

# #4/1

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# user_dict = {user: count for count, user in enumerate(users) if "i" in user}
# sorted = dict(sorted(user_dict.items()))
# print(sorted)

# #EXO XP+ 

# student_grades = {
#     "Alice": [88, 92, 100],
#     "Bob": [75, 78, 80],
#     "Charlie": [92, 90, 85],
#     "Dana": [83, 88, 92],
#     "Eli": [78, 80, 72]
# }


# student_average ={}
# for student in student_grades:
#     average = sum(student_grades[(student)])/len(student_grades[student])
#     student_average[student] = average



# class_average = sum(student_average.values())/len(student_average)
# print(f"moyenne de la classe: {round(class_average)}")
                          



# student_letter_grade = {}
# for student in student_average:
#     if student_average[student] >= 90:
#         student_letter_grade[student] = "A"
#     elif 80 <= student_average[student] <= 89:
#         student_letter_grade[student] = "B"
#     elif 70 <= student_average[student] <= 79:
#         student_letter_grade[student] = "C"
#     elif 60 <= student_average[student] <= 69:
#         student_letter_grade[student] = "D"
#     elif student_letter_grade < 60:
#         student_letter_grade[student] = "F"
#     print(f"{student} à {round(average)} de moyenne générale. Lettre {student_letter_grade[student]}")

# #Ex0 2
 
# sales_data = [
#     {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
#     {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
#     {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
#     {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
#     {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
#     {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
#     {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
# ]

# for each_line in sales_data:
#     each_line["total_price"] = each_line["price"]*each_line["quantity"]
# print(f"1ER TABLEAU :\n {sales_data}\n\n\n")
# transaction_list = [transaction for transaction in sales_data if transaction["total_price"] > 500]
# sales_data.sort(key=lambda x: x["total_price"], reverse=True)

# print(f"2EME TABLEAU : \n{sales_data}")

print()

# total_revenu_by_product = {}
# for sale in sales_data:
#     product = sale["product"]
#     total_price = sale["price"]*sale["quantity"]
#     if product in total_revenu_by_product:
#         total_revenu_by_product[product] += total_price
#     else:
#         total_revenu_by_product[product] = total_price

# print(f"total sales per product: {total_revenu_by_product}")

# total_spent_customers = {}
# for sale in sales_data:
#     customer = sale["customer_id"]
#     total_spent = sale["price"]*sale["quantity"]
#     if customer in total_spent_customers:
#         total_spent_customers[customer] += total_spent
#     else:
#         total_spent_customers[customer] = total_spent

# print(f"total spent by customer: {total_spent_customers}")


