def  ft_water_reminder():
    " ft_water_reminder that asks for the number of days since last watering. If it’s more than 2 days, print Water the plants! otherwise print Plants are ine "
    x = int(input("Days since last watering: "))
    if x > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

ft_water_reminder()