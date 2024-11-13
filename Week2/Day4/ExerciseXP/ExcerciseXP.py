# #Excercice 1: Random Sentence Generator

# import random as r 

# def get_words_from_file():
#     with open('sowpods.txt', 'r+') as file:
#         list_words = [line.strip() for line in file]
#     return list_words
        
#     return clean_lst

# def get_random_sentence(length):
#     words = get_words_from_file()
#     sample_random_lst = r.sample(words, length)
#     random_sentence = ' '.join(sample_random_lst).lower()
#     return random_sentence


    
    

# def main():
#     print(
#                 f"""                        BIENVENUE DANS UN PROGRAMME INNUTILE:
#             CE PROGRAMME VOUS PERMET DE GENERER UNE PHRASE De X MOTS RANDOM""")
#     try:
#         length = int(input("Veuillez entrer un chiffre entre 2 et 20: "))
#         if 2 < length < 20:
#             print(get_random_sentence(length))
#         else:
#             print("veuillez entrer un chiffre entre 2 et 20")
#     except ValueError:
#         print("Erreur ceci n'est pas un nombre valide")
# main()


#Excercise 2: Work with Json

import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sample = json.loads(sampleJson)
salary_value = sample["company"]["employee"]["payable"]["salary"]
print(salary_value)
sample["company"]["employee"]["birthdate"] = "14/12/1988"
print(sample)
sample_json_string = json.dumps(sample, indent=2)
print(sample_json_string)


with open("my_file.json", "w") as path:
    json.dump(sample, path, indent=4)



