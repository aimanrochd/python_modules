import sys


def parse_inventory(args: list) -> dict:
    """Parses command line arguments into an inventory dictionary."""
    inventory = dict()

    for arg in args:
        try:
            parts = arg.split(':')
            if len(parts) != 2:
                raise ValueError("Format must be item:quantity")
            
            name = parts[0]
            quantity = int(parts[1])
            current_qty = inventory.get(name, 0)
            inventory[name] = current_qty + quantity
            
        except ValueError as e:
            print(f"Error parsing '{arg}': {e}")
            continue
            
    return inventory


def get_quantity(item_tuple: tuple) -> int:
    """Helper function to extract quantity for sorting."""
    return item_tuple[1]


def print_analysis(inventory: dict):
    print("=== Inventory System Analysis ===")

    total_items = sum(inventory.values())
    unique_items = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_items}\n")

    print("=== Current Inventory ===")

    sorted_items = sorted(inventory.items(), key=get_quantity, reverse=True)
    for item, quantity in sorted_items:
        if total_items > 0:
            percentage = (quantity / total_items) * 100
        else:
            percentage = 0.0
            
        print(f"{item}: {quantity} units ({percentage:.1f}%)")


def print_statistics(inventory: dict):
    """Finds most and least abundant items using max/min."""
    print("=== Inventory Statistics ===")
    
    if not inventory:
        return
    
    most_abundant = max(inventory, key=inventory.get)
    max_count = inventory[most_abundant]

    least_abundant = min(inventory, key=inventory.get)
    min_count = inventory[least_abundant]

    print(f"Most abundant: {most_abundant} ({max_count} units)")
    print(f"Least abundant: {least_abundant} ({min_count} units)")


def group_categories(inventory: dict) -> dict:
    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }

    for item, quantity in inventory.items():
        if quantity >= 10:
            categories["Abundant"].update({item: quantity})
        elif quantity >= 5:
            categories["Moderate"].update({item: quantity})
        else:
            categories["Scarce"].update({item: quantity})
            
    return categories


def print_categories(categories: dict):
    print("=== Item Categories ===")
    for cat_name, items in categories.items():
        if len(items) > 0:
            print(f"{cat_name}: {items}")


def check_restock(inventory: dict):
    """Identifies items with low stock (quantity < 2)."""
    print("=== Management Suggestions ===")
    
    restock_needed = []
    for item, quantity in inventory.items():

        if quantity < 2:
            restock_needed += [item]
            
    print(f"Restock needed: {restock_needed}")

def show_dict_properties(inventory: dict):
    """Demonstrates dictionary methods as required by output."""
    print("=== Dictionary Properties Demo ===")
    
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    
    search_item = 'sword'
    is_in_inventory = search_item in inventory
    print(f"Sample lookup - '{search_item}' in inventory: {is_in_inventory}")

def main():
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
    print()

if __name__ == "__main__":
    main()