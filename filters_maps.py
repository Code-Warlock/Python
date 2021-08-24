""" Looking into Python Maps and Filters
Anonymous or Lambda Functions
"""
import random
# Filter Functions
# score = [12,23,45,54,26,67,87,91,10]
# # evens = [x for x in score if x % 2 == 0]
# # for each in evens:
# #     print(each)
# # for each in score:
# #     if check(each):
# #         print(each)
# def check(num):
#     """ Function to check if a number is even or not """
#     return num % 2 == 0
# evens = list(filter(check,score))
# for each in evens:
#     print(each)

# Map function
# numbers = 1,2,3,4,5,6,7,8,9
# # ref = [x ** 2 if x % 2 == 0 else x * 2 for x in numbers]
# # for each in numbers:
# #     print(change(each))
# def change(num):
#     """ Function to change a number if it's even or not """
#     if num % 2 == 0:
#         return num ** 2
#     return num * 2
#
# numbers = tuple(map(change,numbers))
# print(numbers)
# def jumble(word):
#     """ Shuffler """
#     word = list(word)
#     random.shuffle(word)
#     word = "".join(word)
#     return word
say_name = lambda name : "اثممخ " + name



print(say_name("Desmond"))
