# #DailyChallenge Day 2

# #Challenge 1

# lst = []
# ask_num = int(input("please enter a number: "))
# ask_len = int(input("please enter a length: "))
# for i in range(1, ask_len + 1):
#      lst.append(ask_num*i)
# print(lst)

#Challenge 2

word = input("please enter a string: ")
new_word = ""
for i in word:
    if len(new_word) == 0 or i != new_word[-1]:
        new_word +=i



    
print(new_word)
