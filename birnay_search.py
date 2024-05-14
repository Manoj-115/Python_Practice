#Binary Search

def binary_search(list,element):
    sorted_list = sorted(list)
    last_value = len(list)-1
    first_ele = 0
    mid = first_ele + (last_value-first_ele) // 2

    if element == mid:
        print(f"The element {element} is present at {mid+1} position")
    elif element >mid:
        for ele in range(mid,last_value):
            if element == sorted_list[ele]:
                print(f"The element {element} is present at {ele+1} position")
    elif element < mid:
        for ele in range(0, mid):
            if element == sorted_list[ele]:
                print(f"The element {element} is present at {ele+1} position")
    else:
        print(f"Element {element} is not present in the list {list}")


list = [21,34,5,6,78,87,4,3,98,45,23,11,12,36,70]
element = int(input("enter the element"))

binary_search(list, element)

