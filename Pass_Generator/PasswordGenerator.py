#Importing random module
import random

#Asking user to input the length of the password to be generated
pass_len=int(input("Enter the length of the password :"))

# Define possible characters manually in a simple way
pass_data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"

# Check if the requested length exceeds the available characters
if pass_len > len(pass_data):
    print("The entered length of the pass cannot exceed than",len(pass_data),"characters.")

else:
    pass_generate=''.join(random.sample(pass_data,pass_len))
    print("Generated password :", pass_generate)