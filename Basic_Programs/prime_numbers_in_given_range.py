#Program to print prime numbers between given range


def prime_numbers(starting_range, ending_range):
    prime_number =[]
    number = starting_range
    while (number <= ending_range):
        count = 0
        for numb in range(2, number):
            if number % numb:
                count += 0
            else:
                count += 1
        if count ==0:
            prime_number.append(number)
        number += 1
    print(f"The prime numbers in the range from {starting_range} to {ending_range} are: \n")
    for element in prime_number:
        print(element, end=", ")

starting_range =int(input("Enter the starting range: "))
ending_range =int(input("Enter the ending range: "))
prime_numbers(starting_range, ending_range)