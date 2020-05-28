print("Todays Date?")
date = input()
print("Breakfast Calories?")
breakfast_calories = int(input())
print("Lunch calories?")
lunch_calories = int(input())
print("Dinner calories?")
dinner_calories = int(input())
print("Snack calories?")
snack_calories = int(input())
total_calories = snack_calories + dinner_calories + lunch_calories + breakfast_calories
print("Calorie count for " + date + ":" + str(total_calories ))


