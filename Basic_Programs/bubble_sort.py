#Bubble sort:

def bubble_sort(list):
    length_of_list = len(list)

    for element in range(length_of_list):
        for elements in range(0, length_of_list-1):
            if list[elements] > list[elements+1]:
                list[elements], list[elements+1] = list[elements+1], list[elements]




lista = [21,32,34,45,67,12,21,78,90,21]
bubble_sort(lista)
print(lista)