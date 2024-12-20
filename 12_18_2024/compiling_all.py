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

def get_charged_batteries():
    print("collecting batteries")
    batteries = [50, 30, 4, 45, 12, 18, 30]  
    minimum_battery_power = 20  
    usable_battery_power = 0   
    usable_battery_count = 0   
    for battery in batteries:  
        if battery > minimum_battery_power:   
            usable_battery_power += battery
            usable_battery_count = usable_battery_count + 1
            if usable_battery_power >=100:
                return usable_battery_power, usable_battery_count


def decrypt_alien_message(alien_message):
    human_message = alien_message[::-1]
    return human_message


def food_divide_equally(foods, crews_member):
    equally_foods = len(foods) // crews_member
    remaining_foods = len(foods) % crews_member
    return equally_foods, remaining_foods

def allien_attack_game():
    print("Welcome to allien attack game")
    print("starting mission.......")

    crews_number, foods = setup_mission()
    print(f"you have {crews_number} astronuts and food available = {foods}")

    print("WELCOME TO THE MARS!!!!!!")

    print("YOUR BATTERY IS DEAD PLEASE CHARGE YOUR BATTERY")
    battery_power, battery_count = get_charged_batteries()
    
    print("Huurray!!! your battery is charged,")
    
    print("OOPS.. Alien has arrived saying:")
    print("rednerrus")

    decrypted_text = decrypt_alien_message("rednerrus")
    print(f"Alien is saying: {decrypted_text}")
    print("Alien has captured all astronuts")

    print("if astronuts wants to escape they have to divide each food and give remaining foods")

    equally_divided, remaining_food = food_divide_equally(foods, crews_number)
    print(f"You have{equally_divided} foods divided equally and remaining = {remaining_food}")
    print("Okay.... Now you can go to Earth")

    print("Mission Completed")

allien_attack_game()