class Text:
    def __init__(self, string):
        self.string = string

    def show_string(self):
        return self.string
    
    def frequency(self, word):
        lst = self.string.split()
        if word in lst:
            frequency = lst.count(word)
            return f"the frequency of the word {word} is {frequency}"
        else:
            return None
        
    def common_word(self):
        lst = self.string.split()
        dico = {word:lst.count(word) for word in lst}
        common_word = max(dico, key=dico.get)
        return f"the most common word i {common_word}"
    
    def unique_word(self):
        lst = self.string.split()
        dico = {word:lst.count(word) for word in lst}
        unique = []
        for key, values in dico.items():
            if values == 1:
                unique.append(key)
        string = " ".join(unique)
        return f"the unique words are: {string}"
    
    @classmethod
    def from_file(cls, name_file):
        with open(name_file, 'r+') as f:
            list_content = f.readlines()
            string = ""
            for line in list_content:
                string += line
        return cls(string)
                




# my_text = Text("A good book would sometimes cost as much as a good house")

# print(my_text.show_string())
# print(my_text.frequency("good"))
# print(my_text.common_word())
# print(my_text.unique_word())
my_txt = Text.from_file('the_stranger.txt')

print(my_txt.frequency("Albert"))


