#python program to count characters in a string:

def count_of_characters(string):
    count = len(string)
    print(f"The number of characters in the given string {string} is {count}")


string = str(input("Enter the string"))
count_of_characters(string)


