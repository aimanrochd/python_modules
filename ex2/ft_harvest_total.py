def  ft_harvest_total():
    "A gardener harvested vegetables on 3 different days ft_harvest_total that asks for the weight of each harvest and calculates the total"
    i = 1
    total = 0;
    for i in range (1, 4):
        total += int(input(f"Day {i} harvest: "))
        i += 1
    print("Total harvest:", total)

ft_harvest_total()