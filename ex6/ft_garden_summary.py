def  ft_garden_summary():
    "ft_garden_summary that asks for a garden name and the number of plants, then displays a simple summary with a fixed status message."
    name = input("Enter garden name: ")
    n = input("Enter number of plants: ")
    print(f"Garden: {name}\nPlants: {n}\nStatus: Growing well!")

ft_garden_summary()