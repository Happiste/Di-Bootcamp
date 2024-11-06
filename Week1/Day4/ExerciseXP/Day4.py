# #Exo 1

# def display_message():
#     print("hey everyOne i'm learning: python basics, conditionals, loops and function in this course")

# display_message()


#exo 2 

# # Write a function called favorite_book() that accepts one parameter called title.
# # The function should print a message, such as "One of my favorite books is <title>".
# # For example: “One of my favorite books is Alice in Wonderland”
# # Call the function, make sure to include a book title as an argument when calling the function.

# def favorite_book(title):
#     print(f"One of my favorite books is {title}")

# favorite_book("Harry des anneaux")

# #Exo 3 

# # Write a function called describe_city() that accepts the name of a city and its country as parameters.
# # The function should print a simple sentence, such as "<city> is in <country>".
# # For example “Reykjavik is in Iceland”
# # Give the country parameter a default value.
# # Call your function.

# def describe_city(city="Jérusalem", country="Israël"):
#     print(f"{city} is in {country}")

# describe_city()

# # Exercise 4 : Random
# # Instructions
# # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
# import random as r

# def compare(num=int(input("enter a number: "))):
#     random_num = r.randint(1,5)
#     print(random_num)
#     print(num)
#     if random_num == num:
#         print(f"whooohouu u chose the right number ! ")
#     else:
#         print("fail")

# compare()


# # 🌟 Exercise 5 : Let’s create some personalized shirts !
# # Instructions
# # Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# # The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# # Call the function make_shirt().

# # Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# # Call the function, in order to make a large shirt with the default message
# # Make medium shirt with the default message
# # Make a shirt of any size with a different message.

# # Bonus: Call the function make_shirt() using keyword arguments.

# def make_shirt(size="L", msg="I love Python"):
#     print(f"the size of the shirt is {size}, and the thext are '{msg}'.")

# make_shirt()
# make_shirt("M")
# make_shirt("L", "I love Israel")
# make_shirt(size="S", msg="Fck Hamas")

# # 🌟 Exercise 6 : Magicians …
# # Instructions
# # Using this list of magician’s names

# # magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# # Create a function called show_magicians(), which prints the name of each magician in the list.
# # Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# # Call the function make_great().
# # Call the function show_magicians() to see that the list has actually been modified.

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# def show_magicians(liste):
#     for name in liste:
#         print(f"name >>>{name}")

# def make_great(liste):
#     for index, name in enumerate(liste):
#         liste[index] = f"The Great {name}" 

# make_great(magician_names)
# show_magicians(magician_names)


# #EXO 7 

# #1/
# import random as r

# def get_random_temp(num=int(input("enter a number: "))):
#     if  num == 12 or 1 <= num <= 2:
#         temp = r.randint(-10, 0)
#         return(temp)
#     elif 3 <= num < 5:
#         temp = r.randint(0, 15)
#         return(temp)
#     elif 6 <= num < 9:
#         temp = r.randint(15, 40)
#         return(temp)
#     elif 9 <= num <= 11:
#         temp = r.randint(0, 15)
#         return(temp)

# #get_random_temp()

# #2/
# def main():
#     temp = get_random_temp()
#     print(f"the temperature right now is {float(temp)} degrees Celsius")
#     if temp < 0: 
#         print(f"Brrr, that’s freezing! Wear some extra layers today")
#     elif 0 <= temp <= 16:
#         print("Quite chilly! Don’t forget your coat")
#     elif 16 < temp <= 23:
#         print("i dont need a coat")
#     elif 23 < temp <= 32:
#         print("wooooo i will wear only a tshirt today")
#     elif 32 < temp <= 40:
#         print("wtf i m going to the swimming pool")

# main()
    
#Exo 8 

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def clean_wrong_answer(lst):
    for question in lst:
        print(f'- {question}')
    return (lst)

def asking_question(**kwargs):
    count = 0
    wrong_answer = []
    for index, question in enumerate(data):
        question = data[index]["question"]
        answer = data[index]["answer"]
        print(f"question {index}: {question}")
        answer_user = input(f">>>> ")
        if answer_user == answer:
            print("Nice one !")
            count += 1
        else:
            print("wrong")
            wrong_answer.append(question)
    print(f"you have {count} points !")
    if wrong_answer:
        print(f"here the question you were wrong:\n", )
        clean_wrong_answer(wrong_answer)
    else: 
        print("Congrats !")

asking_question()