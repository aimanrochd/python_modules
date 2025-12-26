def ft_count_harvest_recursive():
    "should count from 1 to a given number, printing each day until harvest time recursively"

    harvest_day = int(input("Days until harvest: "))
    def recursive_count(current_day):
        if current_day > harvest_day:
            print("Harvest time!")
            return
        print(f"Day {current_day}")
        recursive_count(current_day + 1)

    recursive_count(1)

ft_count_harvest_recursive()