matrix = """    7ii
    Tsx
    h%?
    i #
    sM 
    $a 
    #t%
    ^r!"""


print(matrix)

lst = [list(line) for line in matrix.split('\n')]
print(lst)
















# Transformer chaque ligne en liste de caractères
#lst_matrix = [list(line) for line in matrix.split('\n')]

# Initialiser une liste pour construire le message décrypté
#message = []

# Parcourir chaque colonne
# for col in range(len(lst_matrix[0])):  # Utilise la longueur de la première ligne
#     for row in range(len(lst_matrix)):  # Parcourir chaque ligne
#         char = lst_matrix[row][col]
#         # Ajouter les caractères alphabétiques au message
#         if char.isalpha():
#             message.append(char)
#         # Si un symbole est suivi par une lettre, ajoute un espace
#         elif message and message[-1] != ' ':
#             message.append(' ')

# # Joindre les caractères pour obtenir le message final
# secret_message = ''.join(message).strip()
# print(secret_message)






