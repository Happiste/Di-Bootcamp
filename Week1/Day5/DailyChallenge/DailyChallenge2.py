# import random

# list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
# #rint(list_of_numbers)

# target_number   = 3728

# for i in list_of_numbers:
#     for j in list_of_numbers:
#         k = i+j
#         if k == target_number:
#             print(f"{i} + {j} = {target_number}")

# #fibonacci

# def fib(num):
#   a = 0
#   b = 1
#   for i in range(number)


# print(fib(20))
def generate_numbers():
    yield 1
    yield 2
    yield 3

for num in generate_numbers():
    print(num)
