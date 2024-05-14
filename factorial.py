#TO find factorial of a number:

def factorial(number):
    total = number
    while number>1:
        factor = total
        total = factor * (number-1)
        number -= 1
    print(total)


number = int(input("Enter the number: "))
factorial(number)
