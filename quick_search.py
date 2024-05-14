# Qucik Search

def quick_search(list,element):
    if element in list:
        print(f"{element} is found in the lsist")
    else:
        print(f"{element} is not found in the lsist")


list = [23,45,67,89,12,69,22,43,54,65,34,2,6,9,100]
element = int(input("Enter the element:"))
quick_search(list,element)