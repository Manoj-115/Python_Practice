# Program to change the first element and last element in the lists


def swap_list(list):
    start, *middle, last = list
    print(last,*middle,start)


list = [23, 45, 24, 56, 1, 26, 72]
swap_list(list)
