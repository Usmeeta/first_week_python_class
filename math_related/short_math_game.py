while True:
    try:
        number = int(input("Enter a number: "))
        square = number ** 2
        print(f"The square of {number} is: {square}")
        cube = number ** 3
        print(f"The cube of {number} is: {cube}")
        sum_sq_cube = square + cube
        print(f"The sum of the square and cube is: {sum_sq_cube}")
        user_choice = input("Do you want to continue? (yes/no): ")
        if user_choice == "no":
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")



