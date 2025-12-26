def ft_plant_age():
    "ft_plant_age that asks for a plant’s age in days and tells if it’s ready to harvest (more than 60 days) or not."
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

ft_plant_age()