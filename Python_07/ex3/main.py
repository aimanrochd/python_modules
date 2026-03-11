from ex3.GameEngine import GameEngine
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy


def main() -> None:
    print('=== DataDeck Game Engine ===\n')

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print('Configuring Fantasy Card Game...')
    engine.configure_engine(factory, strategy)
    print('Factory: FantasyCardFactory')
    print(f'Strategy: {strategy.get_strategy_name()}')
    print(f'Available types: {factory.get_supported_types()}')

    print('\nSimulating aggressive turn...')
    hand = [
        factory.create_creature(),
        factory.create_creature('goblin'),
        factory.create_spell()
    ]
    hand_str = ', '.join([f'{c.name} ({c.cost})' for c in hand])
    print(f'Hand: [{hand_str}]')

    print('\nTurn execution:')
    result = engine.simulate_turn()
    print(f'Strategy: {strategy.get_strategy_name()}')
    print(f'Actions: {result}')

    print('\nGame Report:')
    print(engine.get_engine_status())

    print('\nAbstract Factory + Strategy Pattern: '
          'Maximum flexibility achieved!')


if __name__ == '__main__':
    main()
