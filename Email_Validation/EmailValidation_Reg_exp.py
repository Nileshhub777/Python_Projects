import re

email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter email address:")

if re.search(email_condition,user_email):
    print("It's the valid valid email format")
else:
    print("It's the invalid format of email")