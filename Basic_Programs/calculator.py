#Calcaualtor program

def addition(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total
def differnece(numbers):

    numbers = sorted(numbers)
    count = numbers[-1]
    for i in range(0,len(numbers)-1):
        count = count - numbers[i]
    return count
def multiplication(numbers):
    total = 1
    for i in numbers:
        total = total * i
    return total
def division(numbers):
    numbers = sorted(numbers)
    div = numbers[0]
    for i in range(1, len(numbers)):
        div = numbers[i] / div
    return div


number = []
total_numbers = int(input("enter the total numbers"))
for i in range(0,total_numbers):
    i = int(input("Enter the number"))
    number.append(i)

symbols = input("enter the symbol: ")
if symbols == "+":
    print(addition(number))
elif symbols == "-":
        print(differnece(number))
elif symbols == "*":
    print(multiplication(number))
elif symbols == "/":
    print(division(number))
else:
    print("Invalid Symbol")




