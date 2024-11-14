import anagram_checker as a



def main():
    while True: 
        print(">>>>>>ANAGRAM CHECKER<<<<<<")
        print("1. Entrer un mot pour trouver son anagram")
        print("2. Entrer 'quit' pour quitter le programme")
        word = input(">>>")
        if word == 'quit':
            return "Vous avez quitter le programme."
        else:
            my_txt = a.AnagramChecker('sowpods.txt')
            word = word.strip(" ")
            return f"""
            YOUR WORD : '{word.upper()}'
            This is a valid Englis word.
             Anagrams for your word:mea {my_txt.get_anagrams(word)}"""



print(main())