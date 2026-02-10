import sys


def parse_inventory(args: list) -> dict:
    """Parses arguments using split/int for readability."""
    inventory = dict()

    for arg in args:
        try:
            parts = arg.split(':')
            if len(parts) != 2:
                print(f"Error parsing '{arg}': Format must be item:quantity")
                continue

            name = parts[0]
            quantity = int(parts[1])

            current_qty = inventory.get(name, 0)
            inventory[name] = current_qty + quantity
  
        except ValueError:
            print(f"Error parsing '{arg}': Quantity must be a number")
            continue
     
    return inventory


def print_analysis(inventory: dict) -> None:
    print("=== Inventory System Analysis ===")

    total_items = 0
    for qty in inventory.values():
        total_items += qty

    unique_items = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}\n")

    print("=== Current Inventory ===")

    items_list = []
    for k, v in inventory.items():
        items_list += [(k, v)]

    n = len(items_list)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if items_list[j][1] < items_list[j+1][1]:
                items_list[j], items_list[j+1] = items_list[j+1], items_list[j]
            j += 1
        i += 1

    for item, quantity in items_list:
        if total_items > 0:
            percentage = (quantity / total_items) * 100
        else:
            percentage = 0.0
        print(f"{item}: {quantity} units ({percentage:.1f}%)")


def print_statistics(inventory: dict) -> None:
    """Finds most and least abundant items manually (No max/min)."""
    print("=== Inventory Statistics ===")

    if not inventory:
        print("No items to calculate statistics.")
        return

    keys_view = list(inventory.keys())
    first_key = keys_view[0]

    most_abundant = first_key
    least_abundant = first_key
    max_count = inventory[first_key]
    min_count = inventory[first_key]

    for item, quantity in inventory.items():
        if quantity > max_count:
            most_abundant = item
            max_count = quantity

        elif quantity < min_count:
            least_abundant = item
            min_count = quantity

    print(f"Most abundant: {most_abundant} ({max_count} units)")
    print(f"Least abundant: {least_abundant} ({min_count} units)")


def group_categories(inventory: dict) -> dict:
    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }

    for item, quantity in inventory.items():
        if quantity > 5:
            categories["Abundant"].update({item: quantity})
        elif quantity >= 2:
            categories["Moderate"].update({item: quantity})
        else:
            categories["Scarce"].update({item: quantity})
            
    return categories


def print_categories(categories: dict) -> None:
    print("=== Item Categories ===")
    for cat_name, items in categories.items():
        if len(items) > 0:
            print(f"{cat_name}: {items}")


def check_restock(inventory: dict) -> None:
    print("=== Management Suggestions ===")
    restock_needed = []
    for item, quantity in inventory.items():
        if quantity < 2:
            restock_needed += [item]
            
    print(f"Restock needed: {restock_needed}")


def show_dict_properties(inventory: dict) -> None:
    print("=== Dictionary Properties Demo ===")
    
    print(f"Dictionary keys: {[*inventory.keys()]}")
    print(f"Dictionary values: {[*inventory.values()]}")
    
    search_item = 'sword'
    is_in_inventory = search_item in inventory
    print(f"Sample lookup - '{search_item}' in inventory: {is_in_inventory}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item:quantity ...")
        return

    inventory = parse_inventory(sys.argv[1:])
    
    if not inventory:
        return

    print_analysis(inventory)
    print() 
    print_statistics(inventory)
    print() 
    
    cats = group_categories(inventory)
    print_categories(cats)
    print() 
    
    check_restock(inventory)
    print()
    show_dict_properties(inventory)


if __name__ == "__main__":
    main()