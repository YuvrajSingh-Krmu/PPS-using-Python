meals = []
calories = []

while True:
    meal_name = input("Enter the Meal Name: ")
    cal_value = int(input("Enter Calorific Value: "))
    meals.append(meal_name) , calories.append(cal_value)
    last_meal = input("LAST Meal of the day? (yes/no): ")
    if last_meal == 'yes':
       break

print(meals ,"respectively", calories)
total_cal = sum(calories)
print(f"Total\tCalories = {total_cal}")
average_cal = total_cal / len(calories)
print(f"Average\tCalories(perMeal) = {average_cal}")
daily_limit=2500
if total_cal>daily_limit:
    print("Do Not Over-Eat!!!")