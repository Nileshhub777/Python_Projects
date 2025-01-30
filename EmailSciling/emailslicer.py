try:
    email=input("Please enter the email id :").strip()

    if '@' not in email or email.count('@') != 1:
        raise ValueError("Invalid email format !!. Please enter a valid email address.")

    spl1=email.split('@')
    print(spl1)

    username = spl1[0]
    domain_email= spl1[-1]


    if not username or not domain_email:
        raise ValueError ("Invalid email address. Either Username or domain is missing.")

    print(f"Your username is {username} & domain is {domain_email}")

except ValueError as e:
    print(e)

except Exception as e:
    print("An unhandled error has occurred.", e)