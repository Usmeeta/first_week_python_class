def setup_mission():
    print("Setting up for the mission")
    available_foods = ["apple", 
                   "banana", 
                   "watermelon", 
                   "chocolate", 
                   "water", 
                   "grapes", 
                   "pineapple", 
                   "cherry", 
                   "berries", 
                   "cupcakes", 
                   "pestries", 
                   "pizza", 
                   "burger",
                   ]
    available_crew = int(input("Enter available crews"))
    print("Setup completed.......")
    return available_crew, available_foods



def allien_attack_game():
    print("Welcome to allien attack game")
    print("starting mission.......")

    crews_number, foods = setup_mission()
    print(f"you have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!!!")

    print("YOUR BATTERY IS DEAD PLEASE CHARGE YOUR BATTERY")


    print("Mission Completed")

allien_attack_game()