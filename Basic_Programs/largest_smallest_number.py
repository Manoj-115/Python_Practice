numbers = [12,13,45,4,5,61]
largest = smallest =  numbers[0]
for a in numbers:
    if a > largest:
        largest = a
    elif a < smallest:
        smallest = a
print(f"{largest} is the greatest number")
print(f"{smallest} is the greatest number")