from .elements import create_fire, create_water, create_earth
fire_result = create_fire()
water_result = create_water()
earth_result = create_earth()
def healing_potion():
    return f'Healing potion brewed with {fire_result} and {water_result}'

def strength_potion():
    return f'Strength potion brewed with {earth_result} and {fire_result}'

def invisibility_potion():
    return 'Invisibility potion brewed with [air_result] and [water_result]'

def wisdom_potion():
    return 'Wisdom potion brewed with all elements: [all_four_results]'
