def ft_count_harvest_iterative():
    "should count from 1 to a given number, printing each day until harvest time"
    x = int(input("Days until harvest: "))
    i = 1
    while i <= x:
        print(f"Day {i}")
        i += 1
    print("Harvest time!")

ft_count_harvest_iterative()