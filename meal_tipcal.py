meal = float(input("Meal Cost: "))
tip_percent = float(input("Tip %"))
total = meal + (meal * tip_percent / 100) 
print(total)