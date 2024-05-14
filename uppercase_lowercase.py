# Check if given alphabet is in lower/upper case

def uppercase_lowercase(alphabet):
    if alphabet.islower():
        print(f"The given alphabet {alphabet} is lowercase")
    if alphabet.isupper():
        print(f"The given alphabet {alphabet} is uppercase")


alphabet = input("Enter the alphabet:")
uppercase_lowercase(alphabet)