# To find the first 10 odd or even numbers

def odd_even(number):
    odd = []
    even = []
    numb = 2

    while (numb <= number):

        if numb % 2:
            odd.append(numb)
        else:
            even.append(numb)
        numb += 1
    print(f"The first 10 odd numbers are:")
    for element in odd:
        print(element, end=", ")
    print(f"\nThe first 10 even number are;")
    for element in even:
        print(element, end=", ")

number = 20
odd_even(number)