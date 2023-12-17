#Python program to find the simple interest;

def simeple_interesr(p,t,r):
    s_i = (p * t* r) / 100
    print(f'The simple interest is {s_i}')
    print(f"The total amount is :", s_i + p)



principle = int(input("Enter the principle amount : "))
time = int(input("Enter the time period :"))
rate_of_interest = int(input("Enter the rate 0f interest: "))
simeple_interesr(principle,time,rate_of_interest)