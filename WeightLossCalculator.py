def weight_loss(weight, speed, terrain, calories_burned_per_mile, oats_calories, days):
    # Calculate number of miles walked
    miles = speed * 5
    # Multiply miles with terrain factor to get calories burned per day
    if terrain == "Flat":
        calories_burned = miles * calories_burned_per_mile
    elif terrain == "Hilly":
        calories_burned = miles * calories_burned_per_mile * 1.5
    elif terrain == "Uneven":
        calories_burned = miles * calories_burned_per_mile * 2
    elif terrain == "Muddy":
        calories_burned = miles * calories_burned_per_mile * 2.5
    elif terrain == "Rocky":
        calories_burned = miles * calories_burned_per_mile * 3
    else:
        return "Invalid terrain type"
    # Calculate the total calories burned for the week
    total_calories_burned = calories_burned * days
    # Calculate the net calories
    net_calories = oats_calories - total_calories_burned
    # Calculate the weight loss
    weight_loss = net_calories / 3500
    # Check if weight loss is within the recommended range
    if weight_loss < 0.23:
        print('ss',weight - weight_loss)
        return  str((weight - weight_loss) ) + "Weight loss is not sustainable"
    elif weight_loss > 0.9:
        return  str((weight - weight_loss) ) + "{ }Weight loss is harmful"
    else:
        return  str((weight - weight_loss) ) + "{ (weight - weight_loss) } Weight loss is normal"



weight = 110
speed = 5
terrain = "Hilly"
calories_burned_per_mile = 100
oats_calories = 2300
days = 5

#print("Weight loss per week:", weight_loss(weight, speed, terrain, calories_burned_per_mile, oats_calories, days), "kg")
#weight_loss(weight, speed, terrain, calories_burned_per_mile, oats_calories, days)
