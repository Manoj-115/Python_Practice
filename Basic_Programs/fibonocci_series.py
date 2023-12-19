#To print nth number Fibonacci series

def fibonocci_series(number):

    start = 0
    end = 1
    numb = 1
    while(numb <= number):
        print(start,end=", ")
        sum = start + end
        start = end
        end = sum
        numb +=1

number = int(input("Enter the nth number to print fibonocci seried: "))
fibonocci_series(number)
