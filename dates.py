"""Module Docstring"""
import datetime as dt
# datetime===> date
today = dt.date.today()
# year = int(input("Type in your year"))
# month = int(input("Type in your month's number"))
# day = int(input("Type in your birth day"))
# custom = dt.date(year,month,day)
print(f"{today:%a/%b/%y,%j}%")
