print("1. Enter Breakfast Carbs")
print("2. Enter Lunch Carbs")
print("3. Enter Dinner Carbs")

askuser = raw_input("Please select a choice? :")

get_breakfast_carbs = 0
get_lunch_carbs = 0
get_dinner_carbs = 0

if askuser == "1":
        get_breakfast_carbs = int(raw_input("How many carbs did you eat for breakfast? :"))

elif askuser == "2":
        get_lunch_carbs = int(raw_input("How many carbs did you eat for lunch? :"))

elif askuser == "3":
        get_dinner_carbs = int(raw_input("How many carbs did you eat for dinner? :"))


print("Here is your daily carb total: ")
print(get_breakfast_carbs + get_lunch_carbs + get_dinner_carbs)
