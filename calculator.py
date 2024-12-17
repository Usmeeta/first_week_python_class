first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))


user_choice = input("""
                    please choose your option
                    + for additon
                    - for subtraction
                    """)
if user_choice == "+":
  print("Addition = ", first_number + second_number)
elif user_choice == "-":
  print("Subtraction = ", first_number - second_number)
else:
  print("invalid option")



#first munber = int(first number)
print("Addition = ", first_number + second_number)
print("Subtraction = ", first_number - second_number)
print("Multiplication =", first_number * second_number)





