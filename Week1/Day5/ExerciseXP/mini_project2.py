import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
print(word)
    ### YOUR CODE STARTS FROM HERE ###
word = list(word)
answer = list("-"*len(word))
print("Mot à deviner: ", ''.join(answer))


while answer != word:
    ask_letter = input("please enter a letter: ")
    if ask_letter in word:
        for index, letter in enumerate(word):
            if ask_letter == letter:
                answer[index] = ask_letter
                print("good answer!")
                print("Mot à deviner: ", ''.join(answer))
    else:
        print("this letter is not in the word")
        
print("you win !", ''.join(answer))
               

    
        
        
       


