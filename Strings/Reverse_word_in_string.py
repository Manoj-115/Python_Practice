# Python program to reverse words in the string:

def reverse_words(string):
    string2 = ""
    list = string.split()[ :: -1]
    string2 = " ".join(list)
    print(string2)

string = str(input("Enter the String"))
reverse_words(string)