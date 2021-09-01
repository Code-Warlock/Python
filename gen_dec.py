""" Decorators in Python """
# Decorator Function
# def decor(func):
#     """ Function for decorating otherr functions """
#     def wrap():
#         print("=================================================================")
#         print("\t\t\t\t"+func())
#         print("=================================================================")
#     return wrap()
# # def name():
# #     """ example function """
# #     name_val = input("Enter your name : ")
# #     return name_val
#
#
# @decor
# def display():
#     """ example function """
#     return "Tunde"



# """Generators in Python """
# yield
def norms(i):
    """ Functions """
    for each in range(i):
        return each
def give_nums(i):
    """ Function """
    for each in range(i):
        yield each

# for each in give_nums(5):
#     print(each)
# print(tuple(give_nums(20)))
gen = give_nums(6)
a = next(gen)
print(a)
