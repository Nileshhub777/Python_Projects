Target = 901
daily_expenses = 0

for i in range(7):
    expense = int(input(f"Enter Daily expense for day {i+1} :"))
    daily_expenses+=expense

if daily_expenses > Target:
    print("You have exceeded target limit of",Target)
else:
    print("You are within the target limit and Your daily expense and income count is:", daily_expenses)




