""" ATM Module """
class Atm():
    """docstring for Atm Class."""

    def __init__(self):
        raise NotImplementedError("Abstract Class can not be Initialized.")
class SignUp(Atm):
    """docstring forSignUp."""
    _pin = 0
    _username = ""

    def __init__(self, fname,lname,pin):
        self.lastname = lname
        self.firstname = fname
        self.username = self.lastname[0] + self.firstname[0]
        self.pin = pin
        SignUp._pin = self.pin
        SignUp._username = self.username

class Login(SignUp):
    """docstring for Login"""

    def __init__(self, username,pin):
        """ __init__ """
        if username != SignUp._username or pin == SignUp._pin:
            raise NotImplementedError("Details not in the database.")
        self.username = username
        self.pin = pin
