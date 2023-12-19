# Python program to check whether the given string is palindrome or not:

def palindrome(string):

    mid = (len(string)-1) // 2
    first = 0
    last = len(string)-1
    count = 0
    while (first <= mid):
        if string[first] == string[last]:
            first += 1
            last -= 1
        else :
            count = 1
            break
    if count == 0:
        print(f"The Given string {string} is a palindrome")
    else:
        print(f"The Given string {string} is not a palindrome")

def symmetrical(string):
    length_of_string = len(string)
    first = 0
    flag = 0
    if length_of_string % 2 :
        mid = length_of_string // 2 + 1
    else:
        mid = length_of_string //2
    first_half = 0
    second_half = mid
    while (first_half < mid and second_half < length_of_string):
        if string[first_half] == string[second_half]:
            first_half +=1
            second_half += 1
        else:
            flag = 1
            break
    if flag == 0:
        print(f"the given string {string} is symmetrical")
    else:
        print(f"the given string {string} is not symmetrical")


given_string = str(input("Enter the string :"))
palindrome(given_string)
symmetrical(given_string)