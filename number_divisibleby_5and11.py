# Check if a number if divisible by 5 and also 11

def divisible_by(number):
    if number % 5 ==0  and number % 11==0:
        print(f"{number} is divisible by 5 and 11")
    else:
        print(f"{number} is not divisible by 5 and 11")


number = int(input("Enter the number :"))
divisible_by(number)