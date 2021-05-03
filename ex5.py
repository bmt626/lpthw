name = 'Brandon M. Taylor'
age = 34
height = 69 # inches
height_cm = height * 2.54
weight = 220 # totally a lie
weight_kg = 220 * 0.45359237
eyes = 'Green'
teeth = 'White'
hair = "Brownish Red"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {height_cm} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_kg} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the candy.")

# this line is tricky, try to get it exactly right

total = age + height + weight
print(f"If I add {age}, {weight}, and {height} I get {total}.")