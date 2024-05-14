#a way to remove the last object from a list?

def remove_last_objecr_in_list(list):
    list.pop()
    return list


len_of_list = int(input("Enter the length of list:"))
list=[]
print(f"Please enter the {len_of_list} nnumber to the list")
for i in range(0,len_of_list):
    number = int(input())
    list.append(number)
print(f"he list after removing the last eleemnt {remove_last_objecr_in_list(list)}")

