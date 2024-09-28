email=input("Enter the email id :").strip()

spl1=email.split('@')

print(spl1)

username = spl1[0]
domain= spl1[-1]

print(f"Your username is {username} & domain is {domain}")