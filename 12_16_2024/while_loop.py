import random
random_number = random.randint(1, 100)


while True:
    user_guess = int(input("Enter your guess"))
    if user_guess == random_number:
        print("you win")
        break
    elif user_guess < random_number:
        print("Too low")
    else:
        print("Too high")
        user_choice = input("""
                        Do you want to continue? Yes or No 
                    """)
        if user_choice.lower() == "no":
            break      


