principal_amount = float(input("Enter your principal amount: " ))
annual_interest_rate = float(input("Enter your annual interest rate: "))
time_in_years = float(input("Enter your time in years: "))

compound_intrest_rate = float((principal_amount * (1 + (annual_interest_rate / 100))**(time_in_years)) - principal_amount)

print("your compound intrest rate is" , compound_intrest_rate)

