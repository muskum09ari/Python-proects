'''
import datetime
a=int(input("Enter your birth year: "))
age=datetime.datetime.now().year-a
print("ur age is",age,"years old")
'''

import datetime

def cal_age(year,month,day):
    today=datetime.date.today()
    dob=datetime.date(year,month,day)
    age=int((today-dob).days/365)
    return age
    
user_dob=input("enter ur age yyyy-mm-dd in format:")
dob=user_dob.split('-')
print(dob)
year,month,day=int(dob[0]),int(dob[1]),int(dob[2])
your_age=cal_age(year,month,day)
print(f"yours age {your_age} years old")