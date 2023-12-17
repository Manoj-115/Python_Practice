# TO find the nth fibonnocci numbers:
def fibonocci_serires(number):

    a=0
    b = 1
    for fs in range(0, number-1):
        # print(a)
        c = a+b
        a=b
        b=c
    print(a)
number = int(input("Enter the nth number for fibonocci serires:"))
fibonocci_serires(number)