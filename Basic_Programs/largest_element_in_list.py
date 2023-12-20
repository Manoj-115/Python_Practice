#Python Program to find largest element in an array

def largest_element(list):
    largest_number = list[0]
    for number in list:
        if largest_number < number:
            largest_number=number

    print(f'The largest number in the list is {largest_number}')


list =[12, 45, 34, 67, 76, 32, 69, 23, 145, 23, 1]
largest_element(list)
