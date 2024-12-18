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

available_crew = 3

each_crew_food = len(available_foods) // available_crew

remaining_food_count = len(available_foods) % available_crew
print(f"each crew get {each_crew_food} food and remaining food count = {remaining_food_count}")
