""" Index Module """
from tunde_pkg.atm import Atm,SignUp,Login
from colorama import init,Fore,Back
init()
firstname = input("Enter your first name : ")
lastname = input("Enter your last name : ")
pin = int(input("Enter your pin (Four digits only)"))

while True:
    if len(str(pin)) < 4 or len(str(pin)) > 4:
        pin = int(input("Enter your pin (Four digits only)"))
    else:
        break
obj = SignUp(firstname,lastname,pin)
print(obj.pin)
print(obj.username)
try:
    obj2 = Atm()
except Exception as e:
    print(Back.RED + str(e))
