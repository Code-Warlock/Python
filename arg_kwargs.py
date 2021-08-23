""" Arbitary arguments and Arbitary Key word arguments"""
# def palindromes(*args):
#     for each in args:
#         if each.lower() == each.lower()[::-1]:
#             print(f"{each} is a palindrome")
#         else:
#             print(f"{each} is not a palindrome")

# def new(*args):
#     return args
# val = 1,2,3,4,5,6
# first,second,*remnant = val
# print(remnant)


# def say_name(name="",course=""):
#     return f"My name is {name} \nMy course at Aptech is {course}"
# print(say_name(name="Desmond",course="ADSE"))




# def fruits(**kwargs):
#     return kwargs
# print(fruits(favourite="Strawberry",nigerian="Grapes",breakfast="Melon"))



def food(**kwargs):
    """ Kwargs """
    try:
        if kwargs["favourite"]:
            print(kwargs["favourite"])
    except KeyError:
        for key,val in kwargs.items():
            print(f"{key} == {val}")

food(fastfood="Spaghetti",favourite="Irish Potato Chicken Porridge",local_delicacy="Egusi Soup")
