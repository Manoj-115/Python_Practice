#TO find that the given number is armstrog or not:

def armstrong(number):
    given = number
    total = 0
    if number >= 0:
        while given>0:
            temp = given % 10
            total +=temp ** 3
            given = given // 10

    else:
        print("enter more than zero")
    if total == number:
        print(f"THe Given Number {number} is armstrong number")
    else:
        print(f"The given number {number} is not a given number")

number = int(input("enter the number : "))
armstrong(number)


