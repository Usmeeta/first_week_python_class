principal_amount = float(input("Enter your principal amount: " ))
annual_interest_rate = float(input("Enter your annual interest rate: "))
time_in_years = float(input("Enter your time in years: "))
compounding_frequency = float(input("Enter the number of times interest is compounded per year: "))


annual_amount = principal_amount * ((1 + annual_interest_rate/100) / compounding_frequency)**(compounding_frequency*time_in_years)
compound_intrest_rate = annual_amount - principal_amount

print("your compound intrest rate is" , compound_intrest_rate)



