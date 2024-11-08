# #challenge2 

# #EXO 1


# n = 15
# for i in range(n):
#     stars = "*"*(2*i+1)
#     space= " "*(n-i-1)
#     snow_tree = space + stars
#     print(snow_tree)



# n = 15
# for i in range(n):
#     stars = "*"*(i+1)
#     spaces = " "*(n-i)
#     semi_snow_tree = spaces+stars
#     print(semi_snow_tree)


# n = 10
# for i in range(n):
#     stars = "*"*(i + 1)
#     print(stars)
# for i in range(n):
#     stars = "*"*(n-i)
#     spaces = " "*i
#     reverse_stars = spaces + stars
#     print(reverse_stars)


my_list = [455, 2, 24, 12,55, 354, 233] # j'assigne des valeur a my_liste
for i in range(len(my_list) - 1): #je parcours tout ma liste sauf la derniere valeur
    minimum = i # j'affecte a minimum i a chaque iteration minimum vaudra i soit  0, 1, 2, 3
    for j in range( i + 1, len(my_list)):#je parcours de ma liste sur une range entre i+1 et la len de ma liste 
        if(my_list[j] < my_list[minimum]):
            minimum = j
            if(minimum != i):
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]
print(my_list)


