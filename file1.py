# name = "Desmond"
# for letter in name:
#     if letter.lower() == "d":
#         continue
#     else:
#         print(letter)

password = 123456789
user_password = int(input("Enter your password : "))
#
# for each in range(1,10000000000000000000000000000000000000000):
#     if user_password != password:
#         print("Invalid Password!!!")
#         user_password = int(input("Enter your password : "))
#     else:
#         print("Correct Password!")
#         break


while password != user_password:
     print("Invalid Password!!!")
     user_password = int(input("Enter your password : "))
print("Correct Password!")
