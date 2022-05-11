name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
inch_to_centimeter = 2.54
metric_height = round(height * inch_to_centimeter)
lbs_to_kg = 2.2
metric_weight = round(weight / lbs_to_kg)
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {metric_height} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {metric_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")