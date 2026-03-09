from ..elements import create_fire, create_earth

fire_result = create_fire()
earth_result = create_earth()
def lead_to_gold():
    return f'Lead transmuted to gold using {fire_result}'

def stone_to_gem():
    return f'Stone transmuted to gem using {earth_result}'
