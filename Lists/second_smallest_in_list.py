
list = [23,35,26,2,1,56,32]

smallest = list[0]
second_smallest = list[0]
for i in list:
    if i<smallest:
        smallest = i
    for j in list:
        if j < second_smallest and j > smallest:
            second_smallest = j
print(second_smallest)