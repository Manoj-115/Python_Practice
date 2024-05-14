# to find the Sum of an array of numbers:

def sum_array(list):
    sum = 0
    for element in list:
        sum += element
    return sum

list =[]
length_of_list = int(input("enter hte length of list"))
print(f"Enter {length_of_list} number to add to the list")
for ele in range(0,length_of_list):
    element = int(input())
    list.append(element)

print(sum_array(list))