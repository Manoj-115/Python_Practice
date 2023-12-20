#to find the type of an object:

def type_of_element(element, element2, element3):
    print(f"the given element {element} is of {type(element)} type")
    print(f"the given element {element2} is of {type(element2)} type")
    print(f"the given element {element3} is of {type(element3)} type")

element = "Manoj"
element2 = 1234
element3 = [12,43,54,67]
type_of_element(element, element2, element3)