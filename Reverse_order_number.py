# Python program to extract and print digits in reverse order of a number

def reverse(number):
    string =""
    while (number >0):
        temp = number%10
        string += str(temp)
        number= number // 10
    print(int(string))

number = int(input("Enter the number: "))
reverse(number)