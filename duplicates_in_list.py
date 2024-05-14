#Python Program to print duplicates from a list of integers

def duplicates(lista):
    list_b = []

    for element in lista:
        count = 0
        for ele in range(0, len(lista)):
            if element == lista[ele]:
                count += 1
                if count > 1:
                    if element in list_b:
                        pass
                    else:
                        list_b.append(element)

    return list_b


lista = [23, 34, 56, 7, 8, 80, 8, 7, 23, 34, 89, 92, 1, 34, 56,]
print(duplicates(lista))
