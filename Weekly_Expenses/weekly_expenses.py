Target = 899
Total_expenses=0

for i in range(7):
    day_expenses = int(input(f"Expenses on Day {i+1} :"))
    Total_expenses+=day_expenses
print("Total_expenses :", Total_expenses)

if Total_expenses > Target:
    print("You have exceeded the weekly Limit !!")
else:
    print("Yay !! You are within the Target Limit :-) ")


