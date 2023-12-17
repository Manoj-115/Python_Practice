#To find the smallest numebr in the list:

def smallest_number_in_list(lsit):
    smallest = list[0]
    for i in list:
        if i < smallest:
            smallest =i
    return smallest
list = [23,21,56,73,2,45,11,9]
print(smallest_number_in_list(list))