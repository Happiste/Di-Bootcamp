#Challenges

# #Exo 1

# lst = [1, 2, 3, 4, 5, 6]
# print(f"voici la liste de base: {lst}")
# hm_value = int(input("how much value do you want to add ?: "))
# for _ in range(1, hm_value + 1):
#     insert_value = input("que voulez inserer dans la liste ")
#     pos_value = (int(input("a quelle posituon voulez vous inserer la veleur ")) - 1)
#     if insert_value.isnumeric():
#         lst.insert(pos_value, int(insert_value))
#         print(f"liste mise à jour: {lst}")
#     else:
#         lst.insert(pos_value, insert_value)
#         print(f"liste mise à jour: {lst}")

# #Exo2



# def count_space(lst):
#     count = lst.count(' ')
#     return((count))

# def main():
#     sentence = input("rentrer une phrase: ")
#     print(count_space(sentence))
    
# main()
    
#Exo 3 

# lst = [1, 2, 8, 4, 57]

# def my_sum(lst):
#     res = 0
#     for num in lst:
#         if isinstance(num, int):
#             res += num
#         else:
#             continue
#     return(res)
# print(my_sum(lst))


# def my_max(lst):
#     res = lst[0]
#     for index, x in enumerate(lst):
#         if res < x:
#             res = x
#         else:
#             continue
#     return(res)
# # print(my_max(lst))



# def int_input_list():
#     user_input = input("entrer une list: ")
#     my_list = [int(x) for x in user_input if x.isnumeric()]
#     return(my_list)


# print(my_max(int_input_list()))

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(factorial(int(input("entrer un chiffre: "))))

# def list_count(lst, find):
#     count = 0
#     for x in lst:
#         if x == find:
#             count += 1
#         else:
#             continue
#     return count

# print(list_count(["a",1,"a","b"], 1))

# NORM L2

# def norm(lst):
#     sum = 0
#     for x in lst:
#         sum += x**2
#     res = sum**0.5
#     return res 

# print(norm([1,2,3,4,5,6]))

#exo 10 

# lst = ["abcze", "abCD", "abc"]
# def find_longest(lst):
#     longest_word = (lst[0])
#     for i in lst:
#         if len(longest_word) < len(i):
#             longest_word = i
#         else:
#             continue
#     return longest_word


# print(find_longest(lst))

# #Exo 11
# lst = ["John", 34, "Yaël", 23]
# lst_int =[x for x in lst if isinstance(x, int)]
# lst_str = [x for x in lst if isinstance(x, str)]
# print(lst_int)
# print(lst_str)

# #exo12 


# def is_palindrome(word):
#     if word == word[::-1]:
#         print("ton mot est un palindrome")
#     else:
#         print(f"ton mot n'est pas un palindrome: {word[::-1]}")

# is_palindrome("radar")

#Exo 13

    
    
# sentence = "Do or do not there is no try but you are the most beautiful"
# k = 2
# def sum_over_k(sentence, k):
#     count = 0
#     lst_sentence = sentence.split()
#     for x in lst_sentence:
#         if len(x) > k:
#             count +=1
#         else:
#             continue
#     return(count)

# print(sum_over_k(sentence, k))

#Exo 14

# dico = {'a': 1,'b':2,'c':8,'d': 1, "efdf" :13 }
# def dict_avg(dico):
#     somme = 0
#     res = 0
#     for val in dico.values():
#         somme +=val
#     res = somme/len(dico)
#     return(res)

# print(dict_avg(dico))

# #Exo 15

# a = 10 
# b =  20

# def common_div(a, b):
#     lst = []
#     if a > b: 
#         long = range(1, a+1)
#     else:
#         long = range(1, b+1)
#     for i in long: 
#         if a % i == 0 and b % i == 0:
#             lst.append(i)
#         else:
#             continue
#     return(lst)

# print(common_div(10,20))

#exo 16

# def is_prime(num):
#     res = round((num**0.5))
#     is_int = 0
#     for i in range(2, res+1):
#         if num % i == 0:
#             return False
#     return True

    

# print(is_prime(17))


# #Exo 17

# lst = [1,2,2,3,4,5]

# def weird_print(lst):
#     lst = [x for index, x in enumerate(lst) if index % 2 == 0 and x % 2 ==0]
#     return(lst)

# print (weird_print(lst))

# #Exo 18

# def type_count(*args):
#     count_int = 0
#     count_str = 0
#     count_float = 0
#     count_bool = 0
#     count_lst = 0
#     for arg in args:
#         type_arg = type(arg)
#         if isinstance(arg, int):
#             count_int +=1
#         elif isinstance(arg, str):
#             count_str +=1
#         elif isinstance(arg, float):
#             count_float +=1
#         elif isinstance(arg, bool):
#             count_bool +=1
#         elif isinstance(arg, list):
#             count_lst +=1
#     return {
#         "int":count_int,
#         "bool": count_bool,
#         "count": count_float,
#         "str": count_str,
#          "lst": count_lst
#     }

# print(type_count(1, 'string', 1.1, True [1,2,3]))
    
#Exo 18
# var = "salut comment tu vas ?"
# split_var = var.split()
# print(split_var)

# def my_split(sentences, separator=" ")
#     for i in sentences:
#         print(i)
#     return lst

# sentences = "Je m'appelle Jonathan"
# print(sentences.split())
# def my_split(string):
#     lst =[]
#     char =""
#     for i in sentences:
#         if i == ' ':
#             lst.append(char)
#             char = ""
#         else:
#             char += i
#     lst.append(char)        
#     return lst

# print(my_split(sentences))

#Exo 20

def my_password(password):
    hidden_pass = ""
    for char in password:
        hidden_pass += "*"
    return(hidden_pass)

print(my_password(input("enttrer votre password :")))
        
        




  
    



