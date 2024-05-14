#Python program to Count occurrences of an element in a list

def occurence_count(list):

    for element in list:
        count = 0
        for ele in range(0, len(list)):
            if element == list[ele]:
                count += 1
        print(f"The element {element} has occurred {count} times in the list")


list = [21, 23, 43, 23, 12, 21, 45, 54, 45, 67, 67, 23]
occurence_count(list)

