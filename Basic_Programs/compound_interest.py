#Python progrsm to calculate compound interest

def compound_interest(principle, interest_rate, time):
    total_amount= principle *(1 + (interest_rate / 100)) ** time
    ci = total_amount - principle
    print(f"Compound interest for the givena amount {principle} is {ci} and the total amount is {total_amount}")

principle = int(input("Enter the priciple amount: "))
rate_of_interest = int(input("Enter the interest rate: "))
time = int(input("Enter the time period: "))
compound_interest(principle, rate_of_interest, time)