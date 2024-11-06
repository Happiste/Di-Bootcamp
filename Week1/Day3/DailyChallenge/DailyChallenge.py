#DailyChallenge

# word = input("please enter a word: ")
# dico_word = {}
# for index, lettre in enumerate(word):
#     if lettre in dico_word:
#         dico_word[lettre].append(index)
#     else:
#         dico_word[lettre] = [index]

# print(dico_word)

#Challenge 2 
#1/
items_purchase = {
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}

wallet = "$300"
wallet_int = int(wallet.replace("$", ""))

for item, price in items_purchase.items():
    items_purchase[item] = int(price.replace("$", "").replace(",", ""))
print(items_purchase)

for item, price in items_purchase.items():
    print("article", item)
    print("prix", price)

#➞ ["Bread", "Fertilizer", "Water"]

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

#➞ ["Apple", "Bananas", "Fan", "Honey", "Spoon"]

# In fact the prices of Apple + Honey + Fan + Bananas + Pan is more that $100, so you cannot by the Pan, 
# instead you can by the Spoon that is $2

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

#➞ "Nothing"