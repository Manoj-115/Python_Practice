#Python program to interchange first and last elements in a list

def replace_firstandlast_element(list):
    list[0], list[-1] = list[-1], list[0]
    return list


list = [23, 21, 42, 45, 67, 89]
print(replace_firstandlast_element(list))
