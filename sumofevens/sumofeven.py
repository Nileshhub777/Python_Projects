def sumofevens(numbers):
    return sum(num for num in numbers if num % 2 == 0)


numbers = [1,2,3,4,5,6,7,8]
result = sumofevens(numbers)

print("sum result is :",result)