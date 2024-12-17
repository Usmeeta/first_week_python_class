while True:
    number = int(input ("Enter your number:"))
    double = number * 2
    print("the double number is:" , double)
    y = double +10
    print("Adding 10 is: " , y)
    z = y/2
    print("half of y is: " , z)
    a = z - number
    print("subtracting the original :" , a)
    user_choice = input("""
                        Do you want to continue? Yes or No 
                    """)
    if user_choice.lower() == "no":
        break
