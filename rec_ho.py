# import timeit
# # def normal(param):
# #     if type(param) == str:
# #         return param[::-1]
# #     return param ** 2
# # print(normal(3))
#
#
# # Recursion Function
# timeit.timeit('def fib(num):
#     """ Recursion """
#     if num in (0,1):
#         return 1
#     # The very moment of recursion
#     return fib(num-1) + fib(num-2)
# ')
# # Higher Order function
# def show(n):
#     for i in range(n):
#         print(fib(i))
# # show(115)
#
# def run():
#     """ Lamajama """
#     num = 115
#     x = 1
#     y = 1
#     for _ in range(num):
#         print(x)
#         x,y = y,x+y
#         # print(y)





















def wrapper(area):
    print("=============================================================")
    area()
    print("=============================================================")



def calc():
    print(23*3)
wrapper(calc)







def multiply():
    x = 4
    y = 5

    def calculate():
        return x * y
    return calculate()

print(multiply())
