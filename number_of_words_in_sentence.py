#program to find the number of words in the sentence

def words_in_sentence(string):
    list =string.split(" ")
    print(f"The number of words in the given sentence {string} is {len(list)}")


string= str(input("enter the string:"))
words_in_sentence(string)