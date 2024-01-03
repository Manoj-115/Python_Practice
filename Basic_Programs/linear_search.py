#Linear Search

def linear_search(list, number):
    count = 0
    for element in range(len(list)):
        if list[element] == number:
            print(f"The element {number} is present at {element} position")
            count +=1

    if  count == 0:
        print(f"The number {element} is not present in the list {list}")


lsit = [23,45,65,78,12,34,21,89.,67,90,66,55,44]
number = int(input("enter the number:"))
linear_search(lsit, number)