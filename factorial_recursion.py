#Python program ro find the factorial of a number using recursion

def factorial(number):
    if (number==0 or number==1):
        return 1
    else:
        factor = number * factorial(number-1)
    return factor

number = int(input("Enter the number:"))
factor = factorial(number)
print(f"the factorial of number {number} is {factor}")