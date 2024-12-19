temperature = 75

if temperature < 32:
    print("It's freezing!")
elif temperature < 50:
    print("It's cold!")
elif temperature < 70:
    print("It's mild!")
elif temperature < 90:
    print("It's warm!")
else:
    print("It's hot!")

number = int(input("Enter your number: "))

if number % 3 == 0:
    print(f"your number {number} is multiple of 3.")

else:
    print(f"your number {number} is not multiple of 3.")
