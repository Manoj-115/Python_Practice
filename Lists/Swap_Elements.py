#Program to swap two elememts:

def swap_elements(list,pos1,pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = []
length_of_list = int(input("Enter the length of list :"))
for i in range(0,length_of_list):
    j = int(input("Enter the number to list : "))
    list.append(j)
first_position = int(input("enter the first posiiton: "))
second_position = int(input("enter the second posiiton: "))

print(swap_elements(list, first_position, second_position))