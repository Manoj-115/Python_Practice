# program to check the given number is prime:

def prime_number(number):
    numb = 2
    count = 0
    while numb < number:
        if number % numb:
            count += 0
        else:
            count += 1
            break

        numb += 1
    if count == 0:
        print(f"The given number{number} is prime")
    else:
        print(f"The given number{number} is not prime")

number = int(input("Enter the number greater than zero and one:"))
prime_number(number)