def add(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y


print("** Select the operation for Calculator **")
print("1.Add")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter Choice (1/2/3/4) : ")

    if choice in ('1','2','3','4'):
        try:
            num1= float(input("Enter the first number: "))
            num2= float(input("Enter the second number: "))
        except ValueError:
            print("Enter a valid number.")
            continue

        if choice == '1':
            print(num1,"+", num2,"=", add(num1,num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtraction(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))

        next_cal=input("Do you want to do another calculation (yes/no) ?")
        if next_cal == 'no':
            break
    else:
        print("Enter a valid choice !!")







