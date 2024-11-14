# # # Mini-Project: Anagram Checker

# class AnagramChecker:
#     def __init__(self, name_file):
#         with open(name_file, 'r+') as f:
#             self.name_file = name_file
#             self.word_list = f.readlines()
                

#     def is_valid_word(self, word):
#         clean_list = [line.strip()for line in self.word_list]
#         word = word.upper()
#         if word in clean_list: 
#             return True
#         else:
#             return False

#     def is_anagram(self, word1, word2):
#         return sorted(word1) == sorted(word2)       
    
#     def get_anagrams(self, search_word):
#         lst_anagrams=[]
#         if self.is_valid_word(search_word): 
#             clean_list = [line.strip()for line in self.word_list]
#             search_word = search_word.upper()
#             for word in clean_list:
#                 if word != search_word and self.is_anagram(word, search_word):
#                     lst_anagrams.append(word)
#             if not lst_anagrams:
#                 return "0 anagram found"
#         else:
#             return f"{search_word} is not a valid Word"
#         return f"anagram list : {lst_anagrams}"
    

#     def show_txt(self):
#         return self.word_list
    

# if __name__=='__main__':
#     my_txt = AnagramChecker('sowpods.txt')
#     print(my_txt.get_anagrams("meal"))