# import random as r


# class Gene:
#     def __init__(self, value):
#         if value == 0 or value == 1:
#             self.value = value
#         else:
#             print("something went wrong")

#     def mutate(self):
#        self.value = 1 if self.value == 0 else 0

#     def __repr__(self):
#         return str(self.value)

# class Chromosome:
#     def __init__(self):
#         self.genes = [Gene(r.randint(0, 1)) for _ in range(10)]

#     def __str__(self):
#         return ''.join(str(gene) for gene in self.genes)
    
# class DNA:
#     def __init__(self):
#         self.chomosomes = [Chromosome for _ in range(10)]

   

# chromosome = Chromosome()
# print("chomosome", chromosome)
# dna = DNA()



        