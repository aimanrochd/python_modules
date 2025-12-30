def ft_harvest_total():
    total = 0
    # We iterate directly over the list of days
    for day in ["1", "2", "3"]:
        total += int(input(f"Day {day} harvest: "))
    print("Total harvest:", total)


ft_harvest_total()
