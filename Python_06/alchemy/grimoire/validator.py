def validate_ingredients(ingredients: str) -> str:
    valid_elements = {'fire', 'water', 'earth', 'air'}
    provided_items = ingredients.lower().split()
    is_valid = all(item in valid_elements for item in provided_items)
    
    if is_valid and provided_items:
        return f'{ingredients} - VALID'
    else:
        return f'{ingredients} - INVALID'
