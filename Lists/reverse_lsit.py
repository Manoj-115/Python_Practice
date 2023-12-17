#program to find the reverse of a list:

def reverse_list(list):

    reversed_list = list[:: -1 ]
    return reversed_list


list = [32, 1, 45, 67, 87, 37, 34]
print(reverse_list(list))

def reverse_list_using_loop(list):
    i = len(list)
    reversed_list = []
    while(i>0):
        reversed_list.append(list[i-1])
        i -= 1
    return reversed_list
print(reverse_list_using_loop(list))

