#Importing random module
import random

#Asking user to input the length of the password to be generated

pass_len=int(input("enter the length of the password :"))

# Define possible characters manually in a simple way
pass_data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"

pass_generate=''.join(random.sample(pass_data,pass_len))

print(pass_generate)