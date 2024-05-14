#To find odd or even number

def odd_even(number):
    if number % 2 :
        print(f"The given {number} is odd")
    else:
        print(f"The given {number} is even")


number = int(input("Enter the number: "))
odd_even(number)
