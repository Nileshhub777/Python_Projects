#Take user input
usr_input=input("Enter the phrase: ")

#split the user_input into individual words with split()
ind_words=usr_input.split()
#print(ind_words)

#initialize an empty string
a = ""

# for loop to append all acronyms of phrase
for word in ind_words:
    a=a+word[0].upper()
print("The acronym of --> ", usr_input,"is :", a)