# To find the sum of the elements in the list:

def sum_0f_elements(list):
    sum = 0
    for i in list:
        sum = sum+i
    return sum
list = []
length_of_list = int(input("Enter the length_of_lsit; "))
print(f"add {length_of_list} numbers to the lsit")
for number in range(0,length_of_list):
    num = int(input())
    list.append(num)
print(sum_0f_elements(list))