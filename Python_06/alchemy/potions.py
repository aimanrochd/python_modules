from .elements import create_fire, create_water, create_earth, create_air

fire_result = create_fire()
water_result = create_water()
earth_result = create_earth()
air_result = create_air()

def healing_potion():
    return f'Healing potion brewed with {fire_result} and {water_result}'

def strength_potion():
    return f'Strength potion brewed with {earth_result} and {fire_result}'

def invisibility_potion():
    return f'Invisibility potion brewed with {air_result} and {water_result}'

def wisdom_potion():
    return f'Wisdom potion brewed with all elements: {fire_result}, {water_result}, {earth_result}, {air_result}'
