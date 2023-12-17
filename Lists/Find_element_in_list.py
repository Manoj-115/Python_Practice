#program to find the element is presenet in  the list:

def element_present(list, element):
    count = 0
    for i in range (0,len(list)):
        if list[i] == element:
            count += 1
            temp = i + 1

            # print(f"Elemnt  {element} is present in the list")
    if count > 0:
        print(f"Elemnt  {element} is present in the list and is in {temp} posiiton in the lsit")
    else:
        print(f"Elemnt  {element} is not present in the list")

list = []
length_of_list = int(input("Enter the length of list :"))
for i in range(0,length_of_list):
    j = int(input("Enter the number to list : "))
    list.append(j)
element = int(input("enter the element to searh in the list: "))
element_present(list,element)