def addition(number):
    count = 0
    for i in number:
        count = count + i
    return count

def difference(number):
    number = sorted(number)
    count = number[-1]
    for i in range(0, len(number)-1):
        count = count - number[i]
    return count

def multiplication(number):
    count = 1
    for i in numbers:
        count = count * i
    return count
def divison(number):
    number = sorted(number)
    count = number[0]
    for i in range(1, len(number)):
        count = number[i] // count
    return count
numbers = []
total_numbers = int(input("Enter the total nubers:"))
if total_numbers >= 1:
    for i in range(0,total_numbers):
        number = int(input("Enter the Number:"))
        numbers.append(number)

symbol = input("Enter the symbol")
if symbol == "+":
    print(addition(numbers))
if symbol == "-":
    print(difference(numbers))
if symbol == "*":
    print(multiplication(numbers))
if symbol == "//":
    print(divison(numbers))